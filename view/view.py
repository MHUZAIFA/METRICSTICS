# view.py
import tkinter as tk

class MyAppView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        
        # Create and organize your GUI elements here
        self.label = tk.Label(self, text="Hello, Tkinter!")
        self.label.pack()
        
        self.button = tk.Button(self, text="Click me", command=self.controller.handle_button_click)
        self.button.pack()
