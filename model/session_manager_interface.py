# Interface
from abc import ABC, abstractmethod
from typing import List, Optional, Union, Callable, Dict, Any

from model.session_info_parser_interface import SessionInfoParserInterface

class SessionManagerInterface(ABC):
    @abstractmethod
    def get_session_path(self) -> str:
        pass

    @abstractmethod
    def save_session(self, name: str, session_data: List[float], results: Dict[str, float]) -> None:
        pass

    @abstractmethod
    def get_session_by_id(self, session_id: Optional[int] = None) -> Union[None, SessionInfoParserInterface]:
        pass

    @abstractmethod
    def get_all_sessions(self) -> List[Dict[str, Any]]:
        pass
