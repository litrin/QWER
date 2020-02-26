#!/usr/bin/env python

from qwer.perf import MetricCalculator, PerfEventMonitor

#
# DSB ratio requires 2 events, all of those event haven't friendly name in
# perf. It has to build up event from scratch.
#  format: <event_category>/event=<reg_id>,umask=<mask>,name='<friendly name>'/
#

EVENT_LIST = [
    "cpu/event=0x0e,umask=0x01,name='UOPS_ISSUED.ANY'/",
    "cpu/event=0x79,umask=0x08,name='IDQ.DSB_UOPS'/"
]


class DSBRatioCalculator(MetricCalculator):

    def do_calculate(self, events):
        events = events.last  # use the latest values.

        # formula depends friendly names
        values = 100 * events["IDQ.DSB_UOPS"] / events["UOPS_ISSUED.ANY"]
        return "%0.2f%%" % values


if __name__ == "__main__":
    monitor = PerfEventMonitor()

    monitor.set_interval(time_interval=1)
    monitor.set_event_list(EVENT_LIST)

    process = DSBRatioCalculator()
    monitor.set_processor(process)

    monitor.start()
