import time
import unittest

from brexit.queue import Queue

class TestQueue(unittest.TestCase):
    
    def test_add_to_empty_queue_returns_true(self):
        queue = Queue(5, (6, 9))
        truck = 1
        self.assertTrue(queue.add(truck))

    def test_add_to_full_queue_returns_false(self):
        queue = Queue(3, (6, 9))
        self.assertTrue(queue.add(1))
        self.assertTrue(queue.add(2))
        self.assertTrue(queue.add(3))
        self.assertFalse(queue.add(4))

    def test_add_works_after_queue_processed(self):
        queue = Queue(3, (1, 2))
        self.assertTrue(queue.add(1))
        self.assertTrue(queue.add(2))
        self.assertTrue(queue.add(3))
        self.assertFalse(queue.add(4))
        time.sleep(3)
        self.assertTrue(queue.add(4))

    def test_pop_empty_queue(self):
        queue = Queue(3)
        self.assertFalse(queue.pop())

    def test_pop_nonempty_queue(self):
        queue = Queue(3)
        queue.add(1)
        self.assertEquals(1, queue.pop())


class TestConnectedQueues(unittest.TestCase):

    def test_add_to_feeder_queue_then_check_complete_pulls_item_to_second_queue(self):
        feeder_queue = Queue(5)
        customs_queue = Queue(3, delay_range=(1, 2), feeder_queue=feeder_queue)
        feeder_queue.add(1)
        customs_queue.check_complete()
        self.assertEquals(0, feeder_queue.length)
        self.assertEquals(1, customs_queue.length)

    def test_add_two_to_feeder_queue_then_check_complete_pulls_items_to_second_queue(self):
        feeder_queue = Queue(5)
        customs_queue = Queue(3, delay_range=(1, 2), feeder_queue=feeder_queue)
        feeder_queue.add(1)
        feeder_queue.add(2)
        customs_queue.check_complete()
        self.assertEquals(0, feeder_queue.length)
        self.assertEquals(2, customs_queue.length)


class TestParallelConnectedQueues(unittest.TestCase):

    def test_add_4_to_feeder_queue_then_check_complete_pulls_items_to_connected_queues(self):
        feeder_capacity = 4
        feeder_queue = Queue(feeder_capacity)
        customs_queue_1 = Queue(3, delay_range=(1, 2), feeder_queue=feeder_queue)
        customs_queue_2 = Queue(3, delay_range=(1, 2), feeder_queue=feeder_queue)
        for truck in range(feeder_capacity):
            feeder_queue.add(truck+1)
        customs_queue_1.check_complete()
        customs_queue_2.check_complete()
        self.assertEquals(0, feeder_queue.length)
        self.assertEquals(3, customs_queue_1.length)
        self.assertEquals(1, customs_queue_2.length)


class TestUpdateDelayRange(unittest.TestCase):

    def test_enabling_delay_range(self):
        queue = Queue(3)
        queue.add(1)
        time.sleep(3)
        self.assertEquals(1, queue.length)
        queue.update_delay_range((1, 2))
        time.sleep(3)
        self.assertEquals(1, queue.length)


if __name__ == "__main__":
    unittest.main()