# session manager for saving and loading session information
import os
import json
from model.session_info_parser import SessionInfoParser
from model.session_manager_interface import SessionManagerInterface
from typing import Dict, Any, List
import uuid
from datetime import datetime

class SessionManager(SessionManagerInterface):
    
    def __init__(self, sessions_folder, session_file_name):
        self.SESSIONS_FOLDER = sessions_folder
        self.SESSION_FILE_NAME = session_file_name



    def get_session_directory_path(self):
        return os.path.join(self.SESSIONS_FOLDER)
    

    
    def get_session_path(self):
        return os.path.join(self.SESSIONS_FOLDER, self.SESSION_FILE_NAME)
    


    def save_session(self, name: str, results: Dict[str, float]) -> None:

        new_session = self.create_session_item(name=name, results=results)

        file_path = self.get_session_path()

        # Load existing sessions
        existing_sessions = self.get_all_sessions() or []

        # Replace the existing session with the same ID, if it exists
        existing_sessions = [session for session in existing_sessions if session.id != new_session.id]
        existing_sessions.append(new_session)

        # Save the updated sessions to the file
        with open(file_path, 'w') as file:
            json.dump([session.__dict__ for session in existing_sessions], file, indent=2)

        result = self.get_all_sessions()

        print("Session saved successfully!")
        # print(result)

        return result


            
    def create_session_item(self, name: str, results: Dict[str, float]) -> SessionInfoParser:
        # Assuming the session_data format based on the SessionInfoParser
        session_data: Dict[str, Any] = {
            "id": str(uuid.uuid4()),  # Generate a unique identifier
            "name": name,
            "datasetFilePath": self.generate_dataset_filepath(),
            "timestamp": int(datetime.now().timestamp()),
            "results": {
                "min": results["min_value"],
                "max": results["max_value"],
                "mean": results["mean_value"],
                "median": results["median_value"],
                "mode": results["mode_value"],
                "mean_abs_deviation": results["mean_abs_deviation"],
                "std_deviation": results["std_deviation"]
            },  # You may populate this based on your application logic
        }

        # Save the number array as a comma-separated string in a dataset file
        self.save_dataset_file(session_data["datasetFilePath"], results["sorted_data"])

        # Create and return a SessionInfoParser instance
        return SessionInfoParser(session_data)

    def generate_dataset_filepath(self) -> str:
        # Assuming you have a 'sessions' folder at the root level
        sessions_folder = self.get_session_directory_path()

        # Create the 'datasets' folder if it doesn't exist
        dataset_folder = os.path.join(sessions_folder, "datasets")
        os.makedirs(dataset_folder, exist_ok=True)

        # Generate a unique filename for the dataset (you might use additional logic here)
        dataset_filename = str(uuid.uuid4()) + ".txt"

        # Return the full filepath
        return os.path.join(dataset_folder, dataset_filename)

    def save_dataset_file(self, filepath: str, number_array: List[float]):
        # Convert the number array to a comma-separated string
        data_string = ",".join(map(str, number_array))

        # Write the data to the dataset file
        with open(filepath, 'w') as file:
            file.write(data_string)

    def get_session_by_id(self, session_id=None):
        file_path = self.get_session_path()
        try:
            with open(file_path, 'r') as file:
                session_data = json.load(file)
                sessions = [SessionInfoParser(data) for data in session_data]
                if session_id is not None:
                    matching_session = next((session for session in sessions if session.id == session_id), None)
                    return matching_session
                return None # return none if session with session id not found
        except FileNotFoundError:
            return None
        
    def get_all_sessions(self):
        file_path = self.get_session_path()
        try:
            with open(file_path, 'r') as file:
                try:
                    session_data = json.load(file)
                    if not session_data:  # Check if session_data is empty
                        return []
                    return [SessionInfoParser(data) for data in session_data]
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    return []  # Handle the case of invalid JSON
        except FileNotFoundError:
            return None