import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test case for a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test case for a list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test case for a list with a mix of positive and negative integers
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

        # Test case for an empty list
        self.assertIsNone(max_integer([]))

        # Test case for a list with a single element
        self.assertEqual(max_integer([5]), 5)

        # Test case for a list with duplicate elements
        self.assertEqual(max_integer([5, 5, 5]), 5)

        # Test case for a list with floating point numbers
        self.assertEqual(max_integer([1.5, 2.7, 3.9]), 3.9)

        # Test case for a list with a mix of integers and floats
        self.assertEqual(max_integer([1, 2.5, 3, 4.7]), 4.7)

if __name__ == '__main__':
    unittest.main()
