# model class for calculating statistics
from typing import List, Dict
from model.metrics_calculator_interface import MetricsCalculatorInterface

class MetricsCalculator(MetricsCalculatorInterface):
    sorted_data: List[float] = []
    results: Dict[str, float] = None

    def __init__(self) -> None:
        # Initialize any required variables or state
        self.clear_data()
        self.sorted_data = []
    
    def get_results(self) -> Dict[str, float]:
        return self.results


    def calculate_metrics(self, data: List[float]) -> Dict[str, float]:
        # Sort the data
        self.sorted_data = sorted(data)
        length = len(self.sorted_data)

        # Calculate metrics on the entire sorted data
        min_value = self.min(self.sorted_data)
        max_value = self.max(self.sorted_data, length)
        mean_value = self.mean(self.sorted_data, length)
        median_value = self.median(self.sorted_data, length)

        # Mode calculation
        mode_value = self.mode(self.sorted_data)

        # Mean Absolute Deviation calculation
        mean_abs_deviation = self.mad(self.sorted_data, length)

        # Standard Deviation calculation        
        std_deviation = self.standard_deviation(self.sorted_data, length)

        # Return the calculated values as key-value pairs
        self.results = {
            "sorted_data": self.sorted_data,
            "min_value": min_value,
            "max_value": max_value,
            "mean_value": mean_value,
            "median_value": median_value,
            "mode_value": mode_value,
            "mean_abs_deviation": mean_abs_deviation,
            "std_deviation": std_deviation
        }

        return self.results
    
    def min(self, sorted_data):
        return sorted_data[0]
    
    def max(self, sorted_data, length):
        return sorted_data[length - 1]
    
    def mean(self, sorted_data, length):
        return self.calculate_sum(sorted_data) / length
    
    def median(self, sorted_data, length):
        return sorted_data[length // 2]
    
    def mode(self, sorted_data):
        frequency_map = {}
        
        # Count the frequency of each element in the sorted data
        for num in sorted_data:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        
        # Find the maximum frequency without using max function
        max_frequency = 0
        for freq in frequency_map.values():
            if freq > max_frequency:
                max_frequency = freq

        # Find the mode values without using list comprehension
        mode_values = []
        for num, freq in frequency_map.items():
            if freq == max_frequency:
                mode_values.append(num)

        return mode_values
    
    def mad(self, sorted_data, length):
        mean = self.mean(sorted_data, length)
        return self.calculate_sum(self.calculate_absolute_difference(x, mean) for x in self.sorted_data) / length
    
    def standard_deviation(self, sorted_data, length):
        mean = self.mean(sorted_data, length)
        variance = self.calculate_sum((x - mean) ** 2 for x in self.sorted_data) / length
        return self.calculate_square_root(variance) if variance > 0 else 0
    
    def calculate_square_root(self, value):
        # Check if the value is non-negative
        if value >= 0:
            return value ** 0.5
        else:
            raise ValueError("Cannot calculate square root of a negative number")
        
    def calculate_absolute_difference(self, x, mean_value):
        return x - mean_value if x >= mean_value else mean_value - x

    
    def calculate_sum(self, data: List[float]) -> float:
        sum = 0
        for num in data:
            sum += num
        return sum
    
    def find_max_frequency(self, frequency_map):
        # Check if the dictionary is not empty
        if not frequency_map:
            return None

        # Initialize max_value with the first value in the dictionary
        max_value = next(iter(frequency_map.values()))

        # Iterate through the values and update max_value if a larger value is found
        for value in frequency_map.values():
            if value > max_value:
                max_value = value

        return max_value


    def clear_data(self) -> None:
        # Clear instance attributes used for calculated values
        self.min_value = None
        self.max_value = None
        self.mean_value = None
        self.median_value = None
        self.mode_value = None
        self.mean_abs_deviation = None
        self.std_deviation = None
