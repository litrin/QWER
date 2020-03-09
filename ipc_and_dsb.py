#!/usr/bin/env python

import logging

from qwer.perf import BasePerfMetric
from qwer.perf import MetricCalculator, PerfEventMonitor

logging.basicConfig(level=logging.DEBUG)
logging.debug("Enable debugging mode")


# IPC means "instructions per cycle", 2 events are required.
class IPC(BasePerfMetric):
    events = "instructions", "cycles"

    def calculate(self):
        return self["instructions"] / self["cycles"]


class DSB_Ratio(BasePerfMetric):
    events = ("cpu/event=0x0e,umask=0x01,name='UOPS_ISSUED.ANY'/",
              "cpu/event=0x79,umask=0x08,name='IDQ.DSB_UOPS'/")

    def calculate(self):
        return 100 * self["IDQ.DSB_UOPS"] / self["UOPS_ISSUED.ANY"]


if __name__ == "__main__":
    monitor = PerfEventMonitor()

    monitor.set_interval(time_interval=1)  # refresh every 1 second.
    monitor.set_event_list(perf_metrics=[IPC, DSB_Ratio])

    process = MetricCalculator()
    monitor.set_processor(process)

    monitor.start()
