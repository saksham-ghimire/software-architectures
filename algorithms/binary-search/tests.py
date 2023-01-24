import unittest
from main import binarySearch


class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 4
        result = binarySearch(arr, target)
        self.assertEqual(result, 3, f"Expected index not found")

    def test_not_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 6
        result = binarySearch(arr, target)
        self.assertEqual(result, -1, f"Unexpected index found")

    def test_empty_list(self):
        arr = []
        target = 6
        result = binarySearch(arr, target)
        self.assertEqual(result, -1, f"Unexpected index found")

    def test_single_element(self):
        arr = [1]
        target = 1
        result = binarySearch(arr, target)
        self.assertEqual(result, 0, f"Expected index not found")

    def test_not_sorted(self):
        arr = [5, 1, 3, 2, 4]
        target = 3
        result = binarySearch(arr, target)
        self.assertEqual(result, -1, f"Unexpected index found")


if __name__ == "__main__":
    unittest.main()
