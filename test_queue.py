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


if __name__ == "__main__":
    unittest.main()