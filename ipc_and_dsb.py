#!/usr/bin/env python

import logging

from qwer.perf import BasePerfMetric
from qwer.perf import MetricCalculator, PerfEventMonitor

logging.basicConfig(level=logging.DEBUG)
logging.debug("Enable debugging mode")

"""

cpu/event=0x28,umask=0x07,period=200003,name='CORE_POWER.LVL0_TURBO_LICENSE'/
cpu/event=0x28,umask=0x20,period=200003,name=CORE_POWER.LVL2_TURBO_LICENSE/
cpu/event=0x28,umask=0x18,period=200003,name='CORE_POWER.LVL1_TURBO_LICENSE'/

"""


class SIMD_RATIO(BasePerfMetric):
    events = (
        "cpu/event=0x28,umask=0x07,period=200003,name='LVL0'/",
        "cpu/event=0x28,umask=0x20,period=200003,name='LVL2'/",
        "cpu/event=0x28,umask=0x18,period=200003,name='LVL1'/"
    )

    def calculate(self):
        total = self["LVL0"] + self["LVL1"] + self["LVL2"]
        return self["LVL1"] / total, self["LVL2"] / total


if __name__ == "__main__":
    monitor = PerfEventMonitor()

    monitor.set_interval(time_interval=1)  # refresh every 1 second.
    monitor.set_event_list(perf_metrics=[SIMD_RATIO])

    process = MetricCalculator()
    monitor.set_processor(process)

    monitor.start()
