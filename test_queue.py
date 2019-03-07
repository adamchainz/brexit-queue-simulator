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

if __name__ == "__main__":
    unittest.main()