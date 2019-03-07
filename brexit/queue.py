import random
import time


class Queue:
    def __init__(self, size, delay_range=None, feeder_queue=None):
        self.size = size
        self.delay_range = delay_range
        self.ready_time = None
        self.feeder_queue = feeder_queue
        self.queue = []

    @property
    def length(self):
        return len(self.queue)

    def update_delay_range(self, delay_range):
        self.delay_range = delay_range

    def handle_new(self):
        if self.delay_range is not None:
            self.ready_time = time.monotonic() + random.randint(
                *self.delay_range)
    
    def add(self, item):
        assert item
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
        while self.feeder_queue and len(self.queue) < self.size:
            item = self.feeder_queue.pop()
            if not item:
                break
            self.queue.append(item)
            if len(self.queue) == 1:
                self.handle_new()
