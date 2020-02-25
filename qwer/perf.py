from .data_structure
from .data_structure import BaseCollector, BaseProcessor


class PerfStatCollector(BaseCollector):
    last_row_cache = None
    capacity = 2

    process = None
    events = set()
    time_delay = 1 * 1000

    def set_event_list(self, event_list):
        """
        set required perf event metric

        :param metric: BaseMetric
        :return: None
        """
        # make event group
        event_group = "{'%s'}" % ",".join(event_list)
        self.events.add(event_group)
        # self.events = self.events.union(metric.required_perf_events)

    def set_interval(self, interval=1):
        """
        set perf time interval

        :param interval: perf time delay in seconds
        :return: None
        """
        self.time_delay = int(interval * 1000)

    def start_perf(self):
        if len(self.events) is 0:
            raise CollectorError("No perf event selected")

        self.cmd = "perf stat -e %s -A -I %s -x ," % (
            ",".join(self.events), self.time_delay)
        self.process = subprocess.Popen(self.cmd, stderr=subprocess.PIPE,
                                        shell=True)

        row = self.process.stderr.readline()
        self.last_row_cache = row.split(",")

    def __del__(self):
        self.process.kill()  # kill perf process when exit

    def read_outputs(self):
        # example output format:
        # 1.003634245, CPU0, 4299462,, UNC_M_CAS_COUNT.RD, 4800617835, 80.02,,
        metrics = {"ts": self.last_row_cache[0], }

        while True:
            if metrics["ts"] != self.last_row_cache[0]:
                return metrics

            cpu = self.last_row_cache[1]
            metric_name = self.last_row_cache[4]
            metric_value = self.last_row_cache[2]

            if cpu not in metrics.keys():
                metrics[cpu] = {}
            metrics[cpu][metric_name] = metric_value

            row = self.process.stderr.readline()
            self.last_row_cache = row.split(",")

    def do_collect(self):
        if self.process is None:
            self.start_perf()
        elif self.process.poll() is not None:
            exit()

        curr_event = self.read_outputs()
        for k, v in curr_event.items():
            if k == "ts":
                self["ts"] = float(v)
            else:
                self[k] = {a: float(v[a]) for a in v.keys()}


class MetricCalculator(BaseProcessor):

    def do_process(self):
        for k in self.collector.keys():
            if k == "ts":
                self["interval"] = self.collector[k].delta
                continue
            else:
                cpu = k
                events = self.collector[k]
                try:
                    self[cpu] = self.get_metrics(events.last)
                except:
                    return None

    def get_metrics(self, events):
        return events


class PerfEventMonitor:
    interval = 1
    event_list = None
    processor = None

    default_fifo_length = 2

    def set_interval(self, interval=1):
        self.interval = interval

    def set_event_list(self, event_list):
        self.event_list = event_list

    def set_processor(self, processor):
        self.processor = processor

    def start(self):
        if self.processor is None or self.event_list is None:
            return

        collector = PerfStatCollector(self.default_fifo_length)
        collector.set_event_list(self.event_list)
        collector.set_interval(self.interval)

        # Initial processor
        processor = self.processor(self.default_fifo_length)

        # Initial reporter
        reporter = JustPrintReporter()

        # set up collector
        reporter.set_collector(collector)
        # set up processor
        reporter.set_processor(processor)

        reporter.start(self.interval)
