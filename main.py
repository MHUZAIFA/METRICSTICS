# main.py
import model
import controller
import view

if __name__ == "__main__":
    # Create instances of Model, View, and Controller
    # model
    model_session_manager = model.SessionManager(sessions_folder="sessions", session_file_name='session_info.json')
    model_metrics_calculator = model.MetricsCalculator()

    #controller
    main_controller = controller.MainController(model_metrics_calculator, model_session_manager)

    # view
    view = view.MetricsticsGUI(controller=main_controller)

    # Start the Tkinter main loop
    view.run()
