#!/usr/bin/env python

from qwer.perf import MetricCalculator, PerfEventMonitor
from qwer.perf import BasePerfMetric
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Enable debugging mode")


# IPC means "instructions per cycle", 2 events are required.
class IPC(BasePerfMetric):
    events = "instructions", "cycles"

    def calculate(self):
        return self["instructions"] / self["cycles"]


if __name__ == "__main__":
    monitor = PerfEventMonitor()

    monitor.set_interval(time_interval=1)  # refresh every 1 second.
    monitor.set_event_list(perf_metrics=IPC)

    process = MetricCalculator()
    monitor.set_processor(process)

    monitor.start()
