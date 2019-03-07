import random
import time


class Queue:
    def __init__(self, size, delay_range, feeder_queue=None):
        self.size = size
        self.delay_range = delay_range
        self.ready_time = None
        self.feeder_queue = feeder_queue
        self.queue = []

    def update_delay_range(self, delay_range):
        self.delay_range = delay_range

    def handle_new(self):
        self.ready_time = time.monotonic() + random.randint(
            *self.delay_range)
    
    def add(self, item):
        self.check_complete()
        if len(self.queue) < self.size:
            self.queue.append(item)
            if len(self.queue) == 1:
                self.handle_new()
            return True
        return False

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return False

    def check_complete(self):
        if (self.ready_time and self.queue and
            time.monotonic() >= self.ready_time):
            self.queue.pop(0)
            if self.queue:
                self.handle_new()
            else:
                self.ready_time = None
        if len(self.queue) < self.size and self.feeder_queue:
            item = self.feeder_queue.pop()
            if item:
                self.queue.append(item)
                self.handle_new()
