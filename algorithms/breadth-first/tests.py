import unittest
from main import breadth_first


class Test_Breadth_First(unittest.TestCase):
    def test_small_graph(self):
        graph = {1: [2, 3], 2: [1, 4, 5], 3: [4], 4: [6], 5: [2], 6: [], 7: []}
        self.assertEqual(
            breadth_first(graph, 5, 1), "found", f"Expected node not found"
        )

    def test_empty_graph(self):
        graph = {}
        self.assertEqual(
            breadth_first(graph, 5, 1), "not found", f"Unexpected node found"
        )

    def test_disconnected_graphs(self):
        graph = {1: [2, 3], 6: [4, 5]}
        self.assertEqual(
            breadth_first(graph, 6, 1), "not found", f"Unexpected node found"
        )

    def test_cyclic_graphs(self):
        graph = {1: [2], 2: [3], 3: [1]}
        self.assertEqual(
            breadth_first(graph, 2, 3), "found", f"Expected node not found"
        )


if __name__ == "__main__":
    unittest.main()
