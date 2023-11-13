# controller.py
class MyAppController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
    def handle_button_click(self):
        # Define the logic to handle button click, update model, etc.
        new_data = "Button clicked!"
        self.model.update_data(new_data)
        self.update_view()
        
    def update_view(self):
        # Update the view with the latest data from the model
        self.view.label.config(text=self.model.data)

