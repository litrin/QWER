#!/usr/bin/env python

import subprocess

from qwer.perf import MetricCalculator, PerfEventMonitor

EVENT_LIST = [
    "cpu/event=0x0e,umask=0x01,name='UOPS_ISSUED.ANY'/",
    "cpu/event=0x79,umask=0x08,name='IDQ.DSB_UOPS'/"
]


class DSBRatioCalculator(MetricCalculator):

    def do_calculate(self, events):
        events = events.last  # use the latest values.
        values = 100 * events["IDQ.DSB_UOPS"] / events["UOPS_ISSUED.ANY"]
        return "%0.2f%%" % values


if __name__ == "__main__":
    monitor = PerfEventMonitor()
    monitor.set_interval(interval=1)
    monitor.set_event_list(EVENT_LIST)
    monitor.set_processor(DSBRatioCalculator)

    monitor.start()
