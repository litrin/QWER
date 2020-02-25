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
