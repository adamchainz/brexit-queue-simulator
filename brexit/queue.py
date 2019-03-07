import random
import time


class Queue:
    def __init__(self, size, delay_range, feeder_queue=None):
        self.size = size
        self.delay_range = delay_range
        self.ready_time = None
        self.length = 0
        self.feeder_queue = feeder_queue

    def update_delay_range(self, delay_range):
        self.delay_range = delay_range

    def handle_new(self):
        self.ready_time = time.monotonic() + random.randint(6, 9)
    
    def add(self):
        self.check_complete()
        if self.length < self.size:
            self.length += 1
            if self.length == 1:
                self.handle_new()
            return True
        return False

    def pop(self):
        if self.length > 0:
            self.length -= 1
            return True
        return False

    def check_complete(self):
        if (self.ready_time and self.length and
            time.monotonic() >= self.ready_time):
            self.length -=1
            if self.length > 0:
                self.handle_new()
            else:
                self.ready_time = 0
        if self.length < self.size and self.feeder_queue:
            if self.feeder_queue.pop():
                self.length += 1
                self.handle_new()
