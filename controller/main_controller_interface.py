# Interface
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class MainControllerInterface(ABC):
    @abstractmethod
    def calculate_metrics(self, data: Any) -> Any:
        pass

    @abstractmethod
    def clear_data(self) -> None:
        pass

    @abstractmethod
    def get_all_sessions(self) -> None:
        pass

    @abstractmethod
    def save_session(self, name: str) -> None:
        pass

    @abstractmethod
    def load_session(self, session_id: Optional[str] = None) -> Any:
        pass
