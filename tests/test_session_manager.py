import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import json
import uuid
from model.session_manager import SessionManager

class TestSessionManager(unittest.TestCase):

    def setUp(self):
        self.sessions_folder = "sessions"
        self.session_file_name = "session_info.json"
        self.session_manager = SessionManager(self.sessions_folder, self.session_file_name)

    def test_save_session(self):
        results = {
            "min_value": 1.0,
            "max_value": 10.0,
            "mean_value": 5.5,
            "median_value": 4.0,
            "mode_value": 3.0,
            "mean_abs_deviation": 2.0,
            "std_deviation": 2.5,
            "sorted_data": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        }

        expected_session = {
            "id": 'dummy_uuid',
            "name": "Test Session",
            "datasetFilePath": f"{self.sessions_folder}/datasets/dummy_uuid.txt",
            "timestamp": int(datetime.now().timestamp()),
            "results": {
                "min": 1.0,
                "max": 10.0,
                "mean": 5.5,
                "median": 4.0,
                "mode": 3.0,
                "mean_abs_deviation": 2.0,
                "std_deviation": 2.5
            }
        }

        with patch('builtins.open', create=True) as mock_open:
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.read.return_value = json.dumps([expected_session])

            with patch.object(uuid, 'uuid4', return_value='dummy_uuid'):
                self.session_manager.save_session("Test Session", results)

            # Assert that open was called 3 times (for read, for write, and within the test)
            self.assertEqual(mock_open.call_count, 3)

if __name__ == '__main__':
    unittest.main()
