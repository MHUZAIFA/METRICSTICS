# Interface
from abc import ABC, abstractmethod
from typing import List, Tuple, Dict

class MetricsCalculatorInterface(ABC):
    @abstractmethod
    def calculate_metrics(self, data: List[float], chunk_size: int = 1000, max_workers: int = 4) -> Dict[str, float]:
        pass

    @abstractmethod
    def clear_data(self) -> None:
        pass

    @abstractmethod
    def get_results(self) -> Dict[str, float]:
        pass
