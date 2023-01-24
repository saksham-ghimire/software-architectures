import unittest
from main import dijkstra


class DijkstraTest(unittest.TestCase):
    def test_small_connected_graph(self):

        graph = {1: {2: 5, 4: 9}, 2: {3: 2, 4: 3}, 3: {4: 7}, 4: {}}
        start_node = 1
        expected_output = {2: 5, 3: 7, 4: 8}

        output = dijkstra(graph, start_node)

        self.assertEqual(output, expected_output)

    def test_disconnected_graph(self):
        # Set up the graph
        graph = {1: {2: 5, 4: 9}, 2: {3: 2, 4: 3}, 3: {4: 7}, 4: {}}
        start_node = 1
        expected_output = {2: 5, 3: 7, 4: 8}

        # Run the Dijkstra algorithm on the graph
        output = dijkstra(graph, start_node)

        # Compare the output to the expected output
        self.assertEqual(output, expected_output)

    def test_large_graph(self):

        graph = {
            1: {2: 5, 4: 9, 5: 3, 6: 20},
            2: {3: 2, 4: 3, 5: 10},
            3: {4: 7, 5: 8, 6: 30},
            4: {5: 12, 6: 40},
            5: {},
            6: {},
        }
        start_node = 1
        expected_output = {2: 5, 4: 8, 5: 3, 6: 20, 3: 7}

        output = dijkstra(graph, start_node)

        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
