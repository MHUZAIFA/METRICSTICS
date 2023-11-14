# Interface
from typing import Optional, Dict, Any
from abc import ABC, abstractmethod

class SessionInfoParserInterface(ABC):
    @abstractmethod
    def __init__(self, data: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def parse_results(self, results_data: Dict[str, Any]) -> Dict[str, Any]:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
