import unittest
from model.metrics_calculator import MetricsCalculator

class TestMetricsCalculator(unittest.TestCase):

    def setUp(self):
        # Create an instance of the MetricsCalculator for each test
        self.metrics_calculator = MetricsCalculator()

    def test_values_data(self):
        # Test when input data contains positive values
        result = self.metrics_calculator.calculate_metrics([2, 4, 6, 8, 10])
        self.assertEqual(result["sorted_data"], [2, 4, 6, 8, 10])
        self.assertEqual(result["min_value"], 2)
        self.assertEqual(result["max_value"], 10)
        self.assertEqual(result["mean_value"], 6)
        self.assertEqual(result["median_value"], 6)
        self.assertEqual(result["mode_value"], [2, 4, 6, 8, 10])
        self.assertEqual(result["mean_abs_deviation"], 2.4)
        self.assertAlmostEqual(result["std_deviation"], 2.8284, places=4)

    def test_even_number_of_data_points(self):
        # Test when input data contains an even number of data points
        result = self.metrics_calculator.calculate_metrics([2, 4, 6, 8])
        self.assertEqual(result["sorted_data"], [2, 4, 6, 8])
        self.assertEqual(result["min_value"], 2)
        self.assertEqual(result["max_value"], 8)
        self.assertEqual(result["mean_value"], 5)
        self.assertEqual(result["median_value"], 5)
        self.assertEqual(result["mode_value"], [2, 4, 6, 8])
        self.assertEqual(result["mean_abs_deviation"], 2)
        self.assertAlmostEqual(result["std_deviation"], 2.2361, places=4)

    def test_duplicate_values(self):
        # Test when input data contains duplicate values
        result = self.metrics_calculator.calculate_metrics([3, 5, 7, 3, 5, 7])
        self.assertEqual(result["sorted_data"], [3, 3, 5, 5, 7, 7])
        self.assertEqual(result["min_value"], 3)
        self.assertEqual(result["max_value"], 7)
        self.assertEqual(result["mean_value"], 5)
        self.assertEqual(result["median_value"], 5)
        self.assertEqual(result["mode_value"], [3, 5, 7])  # The entire list is a mode
        self.assertAlmostEqual(result["mean_abs_deviation"], 1.3333, places=4)
        self.assertAlmostEqual(result["std_deviation"], 1.63299, places=4)
    
    def test_large_dataset(self):
        # Test when input data contains a large number of data points
        data = list(range(1, 1001))  # A list with numbers from 1 to 100000
        result = self.metrics_calculator.calculate_metrics(data)
        self.assertEqual(result["min_value"], 1)
        self.assertEqual(result["max_value"], 1000)
        self.assertEqual(result["mean_value"], 500.5)
        self.assertEqual(result["median_value"], 500.5)
        self.assertEqual(result["mode_value"], data)  
        self.assertEqual(result["mean_abs_deviation"], 250)
        self.assertAlmostEqual(result["std_deviation"], 288.675, places=3)

if __name__ == '__main__':
    unittest.main()
