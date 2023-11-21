import unittest
from unittest.mock import MagicMock
from controller.main_controller import MainController
from model.metrics_calculator_interface import MetricsCalculatorInterface
from model.session_manager_interface import SessionManagerInterface
from shared.custom_exceptions import ResultsNotAvailableError

class TestMainController(unittest.TestCase):

    def setUp(self):
        self.mock_metrics_calculator = MagicMock(spec=MetricsCalculatorInterface)
        self.mock_session_manager = MagicMock(spec=SessionManagerInterface)
        self.main_controller = MainController(self.mock_metrics_calculator, self.mock_session_manager)

    def test_calculate_metrics(self):
        # Define test data
        test_data = {"key": "value"}
        expected_metrics = {"metric": 42}

        # Mock the behavior of MetricsCalculatorInterface
        self.mock_metrics_calculator.calculate_metrics.return_value = expected_metrics

        # Call the method under test
        actual_metrics = self.main_controller.calculate_metrics(test_data)

        # Check if the method returns the expected value
        self.assertEqual(actual_metrics, expected_metrics)
        self.mock_metrics_calculator.calculate_metrics.assert_called_once_with(test_data)

    def test_clear_data(self):
        # Call the method under test
        self.main_controller.clear_data()

        # Check if the method was called on the mock object
        self.mock_metrics_calculator.clear_data.assert_called_once()

    def test_save_session_with_results(self):
        # Mock that results are available
        self.mock_metrics_calculator.get_results.return_value = {"result": True}

        # Call the method under test
        self.main_controller.save_session("TestSession")

        # Check if the method was called on the mock object
        self.mock_session_manager.save_session.assert_called_once_with(name="TestSession", results={"result": True})

    def test_save_session_without_results(self):
        # Mock that results are not available
        self.mock_metrics_calculator.get_results.return_value = None

        # Call the method under test and check for the expected exception
        with self.assertRaises(ResultsNotAvailableError):
            self.main_controller.save_session("TestSession")

    def test_get_all_sessions(self):
        # Define test data
        expected_sessions = [{"session_id": 1}, {"session_id": 2}]

        # Mock the behavior of SessionManagerInterface
        self.mock_session_manager.get_all_sessions.return_value = expected_sessions

        # Call the method under test
        actual_sessions = self.main_controller.get_all_sessions()

        # Check if the method returns the expected value
        self.assertEqual(actual_sessions, expected_sessions)
        self.mock_session_manager.get_all_sessions.assert_called_once()

    def test_load_session(self):
        # Define test data
        session_id = "123"
        expected_session = {"session_id": session_id, "data": "some_data"}

        # Mock the behavior of SessionManagerInterface
        self.mock_session_manager.get_session_by_id.return_value = expected_session

        # Call the method under test
        actual_session = self.main_controller.load_session(session_id)

        # Check if the method returns the expected value
        self.assertEqual(actual_session, expected_session)
        self.mock_session_manager.get_session_by_id.assert_called_once_with(session_id)

if __name__ == '__main__':
    unittest.main()
