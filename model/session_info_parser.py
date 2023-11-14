from typing import Optional, Dict, Any

from model.session_info_parser_interface import SessionInfoParserInterface

class SessionInfoParser(SessionInfoParserInterface):
    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        self.id: Optional[int] = data.get("id")
        self.name: Optional[str] = data.get("name")
        self.datasetFilePath: Optional[str] = data.get("datasetFilePath")
        self.timestamp: Optional[int] = data.get("timestamp")
        self.results: Dict[str, Any] = self.parse_results(data.get("results", {}))

    def parse_results(self, results_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "min": results_data.get("min"),
            "max": results_data.get("max"),
            "mean": results_data.get("mean"),
            "median": results_data.get("median"),
            "mode": results_data.get("mode"),
            "mean_abs_deviation": results_data.get("mean_abs_deviation"),
            "std_deviation": results_data.get("std_deviation"),
        }

    def __repr__(self) -> str:
        return (
            f"SessionInfoParser(id={self.id}, name={self.name}, "
            f"datasetFilePath={self.datasetFilePath}, timestamp={self.timestamp}, "
            f"results={self.results})"
        )
