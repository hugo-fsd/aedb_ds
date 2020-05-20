import unittest

from aed_ds.lists.doubly_linked_list import DoublyLinkedList
from aed_ds.exceptions import NoSuchElementException

class TestDoublyLinkedListIterator(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()
        self.iterator = self.list.iterator()

    def add_elements(self, quantity, shift=0):
        for i in range(quantity):
            self.list.insert_last(f"element {i+1+shift}")
        self.iterator = self.list.iterator()    

    def test_has_next(self):
        # 0 elements
        self.assertFalse(self.iterator.has_next())

        # 1 elements
        self.add_elements(1)
        self.assertTrue(self.iterator.has_next())

        # 2 elements
        self.add_elements(1)
        self.assertTrue(self.iterator.has_next())

        # 5 elements
        self.add_elements(3)
        self.assertTrue(self.iterator.has_next())

        # iterate to the end and test
        for _ in range(5):
            self.assertTrue(self.iterator.has_next())
            self.iterator.next()
        self.assertFalse(self.iterator.has_next())

        # iterate to the beginning and test

 

        # clear list        
        self.list.make_empty()
        self.iterator = self.list.iterator()
        self.assertFalse(self.iterator.has_next())

    # def test_next(self): pass

    # def test_rewind(self): pass

    # def test_has_previous(self): pass

    # def test_previous(self): pass

    # def test_full_forward(self): pass
