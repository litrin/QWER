#!/usr/bin/env python

from qwer.perf import MetricCalculator, PerfEventMonitor

# IPC means "instructions per cycle", 2 events are required.

EVENT_LIST = [
    "instructions",
    "cycles"
]


class IPCCalculator(MetricCalculator):

    def do_calculate(self, events):
        events = events.last  # use the latest values.
        # formula of IPC
        values = events["instructions"] / events["cycles"]

        return values


if __name__ == "__main__":
    monitor = PerfEventMonitor()

    monitor.set_interval(time_interval=1)  # refresh every 1 second.
    monitor.set_event_list(EVENT_LIST)

    process = IPCCalculator()
    monitor.set_processor(process)

    monitor.start()
