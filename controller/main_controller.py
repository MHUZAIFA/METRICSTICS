# metrics_app/controller/main_controller.py
from typing import Any, Dict, Optional, List
from controller.main_controller_interface import MainControllerInterface, ResultsNotAvailableError
from model.metrics_calculator_interface import MetricsCalculatorInterface
from model.session_manager_interface import SessionManagerInterface
from tkinter import messagebox

class MainController(MainControllerInterface):
    def __init__(self, 
                 metrics_calculator: MetricsCalculatorInterface,
                 session_manager: SessionManagerInterface):
        self.metrics_calculator = metrics_calculator
        self.session_manager = session_manager

    def calculate_metrics(self, data: Any) -> Any:
        metrics = self.metrics_calculator.calculate_metrics(data)
        return metrics
    
    def clear_data(self) -> None:
        self.metrics_calculator.clear_data()

    def get_all_sessions(self) -> List[Dict[str, Any]]:
        return self.session_manager.get_all_sessions()

    def save_session(self, name: str) -> None:
        results = self.metrics_calculator.get_results()
        if results is not None:
            self.session_manager.save_session(name=name, results=results)
        else:
            print("no dataset and results")
            raise ResultsNotAvailableError("Generate results to save a session!")

    def load_session(self, session_id: Optional[str] = None) -> Any:
        return self.session_manager.get_session_by_id(session_id)
