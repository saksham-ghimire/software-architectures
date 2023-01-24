import unittest
from main import quicksort


class TestQuickSort(unittest.TestCase):
    def test_sorted_ascending(self):
        arr = [3, 5, 1, 6, 2, 9, 4, 7, 8]
        result = quicksort(arr)
        self.assertEqual(
            result, [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Expected sorted list not found"
        )

    def test_sorted_descending(self):
        arr = [9, 7, 8, 4, 2, 6, 1, 5, 3]
        result = quicksort(arr)
        self.assertEqual(
            result, [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Expected sorted list not found"
        )

    def test_empty_list(self):
        arr = []
        result = quicksort(arr)
        self.assertEqual(result, [], f"Unexpected result found")

    def test_single_element(self):
        arr = [1]
        result = quicksort(arr)
        self.assertEqual(result, [1], f"Expected sorted list not found")

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = quicksort(arr)
        self.assertEqual(
            result, [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Expected sorted list not found"
        )


if __name__ == "__main__":
    unittest.main()
