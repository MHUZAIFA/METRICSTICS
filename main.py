# main.py
from model.model import MyAppModel
from view.view import MyAppView
from controller.controller import MyAppController

if __name__ == "__main__":
    # Create instances of Model, View, and Controller
    model = MyAppModel()
    view = MyAppView(controller=MyAppController(model, None))
    view.title("Tkinter MVC App")

    # Connect the View to the Controller
    view.controller.view = view

    # Start the Tkinter main loop
    view.mainloop()
