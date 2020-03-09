#
#                    GNU LESSER GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007
#
#  Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
#  Everyone is permitted to copy and distribute verbatim copies
#  of this license document, but changing it is not allowed.
#
#
#   This version of the GNU Lesser General Public License incorporates
# the terms and conditions of version 3 of the GNU General Public
# License, supplemented by the additional permissions listed below.
#
#   0. Additional Definitions.
#
#   As used herein, "this License" refers to version 3 of the GNU Lesser
# General Public License, and the "GNU GPL" refers to version 3 of the GNU
# General Public License.
#
#   "The Library" refers to a covered work governed by this License,
# other than an Application or a Combined Work as defined below.
#
#   An "Application" is any work that makes use of an interface provided
# by the Library, but which is not otherwise based on the Library.
# Defining a subclass of a class defined by the Library is deemed a mode
# of using an interface provided by the Library.
#
#   A "Combined Work" is a work produced by combining or linking an
# Application with the Library.  The particular version of the Library
# with which the Combined Work was made is also called the "Linked
# Version".
#
#   The "Minimal Corresponding Source" for a Combined Work means the
# Corresponding Source for the Combined Work, excluding any source code
# for portions of the Combined Work that, considered in isolation, are
# based on the Application, and not on the Linked Version.
#
#   The "Corresponding Application Code" for a Combined Work means the
# object code and/or source code for the Application, including any data
# and utility programs needed for reproducing the Combined Work from the
# Application, but excluding the System Libraries of the Combined Work.
#
#   1. Exception to Section 3 of the GNU GPL.
#
#   You may convey a covered work under sections 3 and 4 of this License
# without being bound by section 3 of the GNU GPL.
#
#   2. Conveying Modified Versions.
#
#   If you modify a copy of the Library, and, in your modifications, a
# facility refers to a function or data to be supplied by an Application
# that uses the facility (other than as an argument passed when the
# facility is invoked), then you may convey a copy of the modified
# version:
#
#    a) under this License, provided that you make a good faith effort to
#    ensure that, in the event an Application does not supply the
#    function or data, the facility still operates, and performs
#    whatever part of its purpose remains meaningful, or
#
#    b) under the GNU GPL, with none of the additional permissions of
#    this License applicable to that copy.
#
#   3. Object Code Incorporating Material from Library Header Files.
#
#   The object code form of an Application may incorporate material from
# a header file that is part of the Library.  You may convey such object
# code under terms of your choice, provided that, if the incorporated
# material is not limited to numerical parameters, data structure
# layouts and accessors, or small macros, inline functions and templates
# (ten or fewer lines in length), you do both of the following:
#
#    a) Give prominent notice with each copy of the object code that the
#    Library is used in it and that the Library and its use are
#    covered by this License.
#
#    b) Accompany the object code with a copy of the GNU GPL and this license
#    document.
#
#   4. Combined Works.
#
#   You may convey a Combined Work under terms of your choice that,
# taken together, effectively do not restrict modification of the
# portions of the Library contained in the Combined Work and reverse
# engineering for debugging such modifications, if you also do each of
# the following:
#
#    a) Give prominent notice with each copy of the Combined Work that
#    the Library is used in it and that the Library and its use are
#    covered by this License.
#
#    b) Accompany the Combined Work with a copy of the GNU GPL and this license
#    document.
#
#    c) For a Combined Work that displays copyright notices during
#    execution, include the copyright notice for the Library among
#    these notices, as well as a reference directing the user to the
#    copies of the GNU GPL and this license document.
#
#    d) Do one of the following:
#
#        0) Convey the Minimal Corresponding Source under the terms of this
#        License, and the Corresponding Application Code in a form
#        suitable for, and under terms that permit, the user to
#        recombine or relink the Application with a modified version of
#        the Linked Version to produce a modified Combined Work, in the
#        manner specified by section 6 of the GNU GPL for conveying
#        Corresponding Source.
#
#        1) Use a suitable shared library mechanism for linking with the
#        Library.  A suitable mechanism is one that (a) uses at run time
#        a copy of the Library already present on the user's computer
#        system, and (b) will operate properly with a modified version
#        of the Library that is interface-compatible with the Linked
#        Version.
#
#    e) Provide Installation Information, but only if you would otherwise
#    be required to provide such information under section 6 of the
#    GNU GPL, and only to the extent that such information is
#    necessary to install and execute a modified version of the
#    Combined Work produced by recombining or relinking the
#    Application with a modified version of the Linked Version. (If
#    you use option 4d0, the Installation Information must accompany
#    the Minimal Corresponding Source and Corresponding Application
#    Code. If you use option 4d1, you must provide the Installation
#    Information in the manner specified by section 6 of the GNU GPL
#    for conveying Corresponding Source.)
#
#   5. Combined Libraries.
#
#   You may place library facilities that are a work based on the
# Library side by side in a single library together with other library
# facilities that are not Applications and are not covered by this
# License, and convey such a combined library under terms of your
# choice, if you do both of the following:
#
#    a) Accompany the combined library with a copy of the same work based
#    on the Library, uncombined with any other library facilities,
#    conveyed under the terms of this License.
#
#    b) Give prominent notice with the combined library that part of it
#    is a work based on the Library, and explaining where to find the
#    accompanying uncombined form of the same work.
#
#   6. Revised Versions of the GNU Lesser General Public License.
#
#   The Free Software Foundation may publish revised and/or new versions
# of the GNU Lesser General Public License from time to time. Such new
# versions will be similar in spirit to the present version, but may
# differ in detail to address new problems or concerns.
#
#   Each version is given a distinguishing version number. If the
# Library as you received it specifies that a certain numbered version
# of the GNU Lesser General Public License "or any later version"
# applies to it, you have the option of following the terms and
# conditions either of that published version or of any later version
# published by the Free Software Foundation. If the Library as you
# received it does not specify a version number of the GNU Lesser
# General Public License, you may choose any version of the GNU Lesser
# General Public License ever published by the Free Software Foundation.
#
#   If the Library as you received it specifies that a proxy can decide
# whether future versions of the GNU Lesser General Public License shall
# apply, that proxy's public statement of acceptance of any version is
# permanent authorization for you to choose that version for the
# Library.
#

import subprocess
from abc import ABCMeta

from .data_structure import BaseCollector, BaseProcessor, BaseReporter, \
    CollectorError


class BasePerfMetric(dict):
    __metaclass__ = ABCMeta
    events = "a", "b"
    _formula = "a+b"

    def calculate(self):
        formula = self._formula
        for event in self.events:
            _event = "self['%s']" % event
            formula = formula.replace(event, _event)

        return eval(formula)

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def value(self):
        try:
            return self.calculate()
        except:
            return None

    def __str__(self):
        return "%s: %0.2f" % (self.name, self.value)


class PerfStatCollector(BaseCollector):
    last_row_cache = None
    capacity = 2

    perf_process = None
    events = set()
    time_delay = 1 * 1000
    aggregate_mode = False
    cpu_cores = None

    perf_metrics = []

    def add_metrics(self, metric):
        if not isinstance(metric, BasePerfMetric):
            raise CollectorError("Metric is invalid!")

        self.perf_metrics.append(metric)
        self.set_event_list(list(metric.events))

    def set_event_list(self, event_list):
        """
        set required perf event metric

        :param metric: BaseMetric
        :param aggregate_mode: bool enabled/disable perf aggregate "-A"
        :return: None
        """
        # make event group
        event_group = "{'%s'}" % ",".join(event_list)
        self.events.add(event_group)

    def set_aggregate_mode(self, mode):
        """
        Enable/disable system level aggregation

        :param mode: bool
        :return:
        """
        self.aggregate_mode = mode

    def set_cpu_cores(self, cpu_cores):
        """
        Set cores would be monitored

        :param cpu_cores: str coreset like 1,2,3 or 1-3
        :return: None
        """
        self.cpu_cores = cpu_cores

    def set_interval(self, interval=1):
        """
        set perf time time_interval

        :param interval: perf time delay in seconds
        :return: None
        """
        self.time_delay = int(interval * 1000)

    def start_perf(self):
        if len(self.events) is 0:
            raise CollectorError("No perf event selected")

        # build up perf stat command with:
        #   -e <event list>
        #   -A  NO aggregation
        #   -I  refresh in ms
        #   -x , csv style output
        self.cmd = "perf stat -e %s  -I %s -x ," % (
            ",".join(self.events), self.time_delay)

        if not self.aggregate_mode:
            self.cmd = "%s -A" % self.cmd

        if self.cpu_cores is not None:
            self.cmd = "%s -C %s" % (self.cmd, self.cpu_cores)

        # Start perf, capture outputs from stderr
        self.perf_process = subprocess.Popen(self.cmd, stderr=subprocess.PIPE,
                                             shell=True)

        row = self.perf_process.stderr.readline()
        self.last_row_cache = row.split(",")

    def __del__(self):
        self.perf_process.kill()  # kill perf process when exit

    def read_outputs(self):
        # example output format:
        metrics = {"ts": self.last_row_cache[0], }

        while True:
            if metrics["ts"] != self.last_row_cache[0]:
                # break if timestamp changed
                break

            if self.aggregate_mode:
                cpu = "system_aggregation"
                metric_name = self.last_row_cache[3]
                metric_value = self.last_row_cache[1]
            else:
                cpu = self.last_row_cache[1]
                metric_name = self.last_row_cache[4]
                metric_value = self.last_row_cache[2]

            if cpu not in metrics.keys():
                metrics[cpu] = {}

            metrics[cpu][metric_name] = metric_value
            row = self.perf_process.stderr.readline()

            self.last_row_cache = row.split(",")

        return metrics

    def do_collect(self):
        if self.perf_process is None:
            self.start_perf()
        elif self.perf_process.poll() is not None:
            exit()

        curr_event = self.read_outputs()

        for k, v in curr_event.items():
            if k == "ts":
                self["ts"] = float(v)
                continue

            telemetries = {a: float(v[a]) for a in v.keys()}

            if len(self.perf_metrics) is 0:
                # No perf metrics needed
                self[k] = telemetries
            else:
                self[k] = self.combine_perf_metrics(telemetries)

    def combine_perf_metrics(self, t):
        metric_data = {}
        for metric in self.perf_metrics:
            metric_data[metric.name] = metric(t)

        return metric_data


class MetricCalculator(BaseProcessor):
    capacity = 2

    def do_process(self):
        for k in self.collector.keys():
            if k == "ts":
                self["time_interval"] = self.collector[k].delta
                continue
            else:
                cpu = k
                events = self.collector[k]
                try:
                    self[cpu] = self.do_calculate(events)
                except:
                    return None

    def do_calculate(self, events):
        """
        Metric formula
        :param events: dict, grouped event counter values
        :return: values
        """
        return events.last.value


class PerfEventMonitor(BaseReporter):
    interval = 1

    def set_interval(self, time_interval=1):
        self.interval = time_interval

    def set_event_list(self, event_list=None, perf_metrics=None,
                       aggregation_mode=None):
        collector = PerfStatCollector()

        collector.set_interval(self.interval)

        if event_list is not None:
            collector.set_event_list(event_list)
        if perf_metrics is not None:
            if not issubclass(perf_metrics, BasePerfMetric):
                for i in perf_metrics:
                    collector.add_metrics(i)
            else:
                collector.add_metrics(perf_metrics)

        if aggregation_mode is not None:
            collector.set_aggregate_mode(aggregation_mode)

        self.set_collector(collector)

    def do_report(self, processor):
        print(processor)
