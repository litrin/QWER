import collections
import random
import time
from abc import ABCMeta, abstractmethod

__all__ = ["BaseCollector", "BaseProcessor", "BaseReporter",
           "DoNothingProcessor", "JustPrintReporter", "FakeCollector"]


class FIFOList:
    """
    FIFO queue
    """
    data = None
    capacity = None
    count = 0

    def __init__(self, length):
        """
        Initial a FIFO with length

        :param length: int
        """
        self.capacity = length
        self.data = collections.deque([0])

    def append(self, value):
        self.count += 1
        if self.count > self.capacity:
            self.data.popleft()

        return self.data.append(value)

    @property
    def is_increasing(self):
        try:
            return self.data[-1] > self.data[-2]
        except IndexError:
            return True

    @property
    def slop(self):
        try:
            return float(self.data[-1] - self.data[-2]) / self.data[-2]
        except IndexError:
            return 1.0

    @property
    def delta(self):
        try:
            return self.data[-1] - self.data[-2]
        except IndexError:
            return 0

    @property
    def last(self):
        return self.data[-1]

    @property
    def sum(self):
        return sum(self.data)

    def __repr__(self):
        return "%s" % (self.data[-1])

    def __str__(self):
        return str(self.last)

    def __len__(self):
        return self.count


class FIFOGroup(dict):
    """
    Multiple FIFO queue container, key-value style follow dicts.
    """
    capacity = 0
    Content = FIFOList

    def __init__(self, capacity=0):
        self.capacity = capacity

    def __getitem__(self, k):
        if k not in self.keys():
            self[k] = self.Content(self.capacity)

        return super(FIFOGroup, self).__getitem__(k)

    def __setitem__(self, k, v):
        if k not in self.keys():
            super(FIFOGroup, self).__setitem__(k,
                                               self.Content(self.capacity))

        super(FIFOGroup, self).__getitem__(k).append(v)

    def __repr__(self):
        return str({k: v.last for k, v in self.items()})

    def __len__(self):
        return self.capacity


class CollectorError(Exception):
    pass


class ProcessorError(Exception):
    pass


class ReporterError(Exception):
    pass


class BaseCollector(FIFOGroup):
    __metaclass__ = ABCMeta
    monitor_groups = []

    def set_mon_group(self, mon_groups):
        """
        Set monitoring groups

        :param mon_groups: list
        :return:
        """
        self.monitor_groups = mon_groups
        # self.refresh()

    @abstractmethod
    def do_collect(self):
        """
        Refresh telemetries
        :return:
        """
        pass


class BaseProcessor(FIFOGroup):
    __metaclass__ = ABCMeta

    collector = None
    is_running = True

    def set_collector(self, collector):
        self.collector = collector
        self.collector.do_collect()

    def __iter__(self):
        while self.is_running:
            self.collector.do_collect()
            self.do_process()
            yield self

    @abstractmethod
    def do_process(self):
        pass

    def stop(self):
        self.is_running = False


class BaseReporter:
    __metaclass__ = ABCMeta
    collector = None
    processor = None

    counter = 0
    report_frequency = 1

    def set_collector(self, collector):
        if isinstance(collector, BaseCollector):
            self.collector = collector
        else:
            raise ReporterError(
                "Argument for method is not a type of collector!")

    def set_processor(self, processor):
        if isinstance(processor, BaseProcessor):
            self.processor = processor
        else:
            raise ReporterError(
                "Argument for method is not a type of collector!")

    def start(self, time_interval=1):
        self.processor.set_collector(self.collector)
        for current in self.processor:
            self.counter += 1

            # do report frequently
            if self.counter % self.report_frequency is (
                    self.report_frequency - 1):
                self.do_report(current)

            time.sleep(time_interval)

    @abstractmethod
    def do_report(self, processor):
        pass


class FakeCollector(BaseCollector):
    """
    Example codes: Generate random int in range
    """
    random_range = (1, 1024)

    def set_random_range(self, int_min, int_max):
        if int_max < int_min:
            int_min, int_max = int_max, int_min
        self.random_range = (int_min, int_max)

    def do_collect(self):
        for k in self.monitor_groups:
            self[k] = random.randint(self.random_range[0],
                                     self.random_range[1])

        # print self
        # self.collection[k] = (float(content) - self.collection[k].last)


class DoNothingProcessor(BaseProcessor):
    """
    Example codes: do nothing, copy data from collector to process
    """
    def do_process(self):
        for k, v in self.collector.items():
            self[k] = v


class JustPrintReporter(BaseReporter):
    """
    Example codes: print out data from process
    """
    def do_report(self, processor):
        print(processor)
