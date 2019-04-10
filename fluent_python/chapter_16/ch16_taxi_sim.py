#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/12 14:58
from collections import namedtuple
import queue
DEPARTURE_INTERVAL = 5

Event = namedtuple('Event', 'time proc action')


def taxi_process(ident, trips, start_time=0):
    """
    You can test this function at the terminal like this:
    from chapter_16.ch16_taxi_sim import taxi_process
    taxi = taxi_process(ident=13, trips=2)
    next(taxi)
    taxi.send(_.time + 7)
    :param ident: taxi no
    :param trips: the numbers of taxi trips
    :param start_time: start time
    :return:
    """
    time = yield Event(start_time, ident, 'leave garage')
    for _ in range(trips):
        time = yield Event(time, ident, 'pick up a passenger')
        time = yield Event(time, ident, 'drop off a passenger')
    yield Event(time, ident, 'going home')


def compute_duration():
    """
    calculate next time of the event
    """
    pass


class Simulator:
    """
    simulator
    The Discrete Event Simulation(DES)
    """

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        for _, proc in self.procs.items():
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('tax_id: ', proc_id, proc_id * ' ', previous_action)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration()
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


if __name__ == "__main__":
    num_taxis = 3
    taxis = {
        i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL) for i in range(num_taxis)
    }
    sim = Simulator(taxis)
    sim.run(180)
