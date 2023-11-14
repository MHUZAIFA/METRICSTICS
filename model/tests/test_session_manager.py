import unittest
import os
from ..implementations.session_manager import SessionManager
from ..implementations.session_info_parser import SessionInfoParser

class TestSessionManager(unittest.TestCase):
    def setUp(self):
        # Create an instance of SessionManager with a test folder and filename
        self.test_folder = 'test_sessions'
        self.test_filename = 'test_session_info.json'
        self.session_manager = SessionManager(sessions_folder=self.test_folder, session_file_name=self.test_filename)

    def tearDown(self):
        # Clean up: Delete the test session file and folder
        file_path = self.session_manager.get_session_path()
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(self.test_folder):
            os.rmdir(self.test_folder)

    def test_save_and_load_session(self):
        # Create a test session
        test_session_id = 'test_session_123'
        test_session_data = {'id': test_session_id, 'attribute': 'value'}
        test_session = SessionInfoParser(test_session_data)

        # Save the test session
        self.session_manager.save_session(test_session)

        # Load the saved session by ID
        loaded_session = self.session_manager.load_session(session_id=test_session_id)

        # Assert that the loaded session is not None and has the correct ID
        self.assertIsNotNone(loaded_session)
        self.assertEqual(loaded_session.id, test_session_id)

    def test_get_all_sessions(self):
        # Create and save multiple test sessions
        test_sessions = [
            {'id': 'session_1', 'attribute': 'value1'},
            {'id': 'session_2', 'attribute': 'value2'},
            {'id': 'session_3', 'attribute': 'value3'}
        ]

        for session_data in test_sessions:
            test_session = SessionInfoParser(session_data)
            self.session_manager.save_session(test_session)

        # Get all sessions and assert that the number of loaded sessions matches the number of saved sessions
        all_sessions = self.session_manager.get_all_sessions()
        self.assertEqual(len(all_sessions), len(test_sessions))

if __name__ == '__main__':
    unittest.main()
