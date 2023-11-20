import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import Listbox
from tkinter import ttk
from tkinter.messagebox import askyesno
import random
from random import randint
import os
from tkinter import font
from datetime import datetime, timedelta
import controller
import re
from tkinter import PhotoImage
from tkinter import messagebox
from shared.custom_exceptions import ResultsNotAvailableError

primaryBgColor = '#171717'
primaryBtnBgColor = '#272727'
primaryBtnSelectedBgColor = '#195AC4'
secondaryBtnSelectedBgColor = '#272727'

descriptive_statistics_notes = """
Usage:

User can feed data to the system in 3 ways:
1. Through keyboard,
2. Through a file and
3. Using inbuilt Auto functionality that generates random number

Users can save and load sessions using the save button and by clicking on a previous stored session in column 3 section 2 of the application.

Notes: 
1. The keyboard and file input(s) need to be comma seperated. 
2. The calculated statistics are rounded to two decimal places.


Description:

Metristics helps in calculating descriptive statistics.

The purpose of descriptive statistics is to quantitatively describe a collection of data by measures of central tendency, measures of frequency, and measures of variability.

Let x be a random variable that can take values from a finite data set x1, x2, x3, ..., xn, with each value having the same probability.

1. The minimum, m, is the smallest of the values in the given data set. (m need not be unique.)

2. The maximum, M, is the largest of the values in the given data set. (M need not be unique.)

3. The mode, o, is the value that appears most frequently in the given data set. (o need not be unique.)

4. The median, d, is the middle number if n is odd, and is the arithmetic mean of the two middle numbers if n is even.

5. Mean (μ):
   μ = (1/n) * Σ(xi), where i ranges from 1 to n.

6. Mean Absolute Deviation (MAD):
   MAD = (1/n) * Σ |xi - μ|, where i ranges from 1 to n.

7. Standard Deviation (σ):
   σ = sqrt((1/n) * Σ(xi - μ)^2), where i ranges from 1 to n.
"""



class ScrollableLabelFrame:
    def __init__(self, master, heading, content):
        self.master = master
        self.heading = heading
        self.content = content

        # Create a frame
        self.frame = tk.Frame(master, bg=primaryBgColor)  # Background color can be adjusted

        if self.heading:
            # Add a heading label
            self.heading_label = tk.Label(self.frame, text=self.heading, font=("Helvetica", 16), bg=primaryBgColor, foreground="white")
            self.heading_label.pack(side="top", anchor="w", pady=10)  # Add padding only at the top

        # Create a text widget for the scrollable label
        self.scrollable_label = tk.Text(self.frame, wrap="word", width=40, height=20, padx=10, pady=10, state="disabled", font=("Helvetica", 14), background=primaryBgColor, foreground="white")
        self.scrollable_label.pack(side="left", fill="both", expand=True)

        # Add a scrollbar to the textarea
        text_scrollbar = ttk.Scrollbar(self.frame, command=self.scrollable_label.yview)
        text_scrollbar.pack(side="right", fill="y")

        # Create a custom style for the scrollbar
        scrollbar_style = ttk.Style()
        scrollbar_style.configure("TScrollbar")

        # Apply the custom style to the scrollbar
        text_scrollbar.config(style="TScrollbar")
        self.scrollable_label.configure(state="normal")
        self.scrollable_label.insert(tk.END, self.content)
        self.scrollable_label.config(yscrollcommand=text_scrollbar.set, highlightbackground=primaryBtnBgColor, highlightcolor=primaryBtnBgColor, insertbackground='white', state="disabled")

    def setContent(self, value):
        self.content = value
        self.scrollable_label.configure(state="normal")
        self.scrollable_label.delete(1.0, tk.END)
        self.scrollable_label.insert(tk.END, self.content)
        self.scrollable_label.configure(state="disabled")



class InfoCard:
    def __init__(self, master, number, title):
        self.master = master
        self.number = number
        self.title = title
        self.row_frame = None

        self.row_frame = tk.Frame(self.master, bg=primaryBtnBgColor, pady=10, padx=0)  # Blue background color for visibility

        # Create a label to display the number on top
        self.number_label = tk.Label(self.row_frame, text=str(self.number), bg=primaryBtnBgColor, fg="#ffffff", font=("Helvetica", 36), width=8, height=2)
        self.number_label.pack(pady=(10, 0), padx=0)  # Add padding only at the top

        # Create a label to display the title on the bottom
        title_label = tk.Label(self.row_frame, text=self.title, bg=primaryBtnBgColor, fg="#ffffff")
        title_label.pack(pady=(0, 10))  # Add padding only at the bottom

    def grid(self, row, column):
        self.row_frame.grid(row=row, column=column, padx=10)

    def update_number(self, new_number):
        if new_number % 1 == 0:
            # If the new number is an integer, display it without decimal places
            self.number = str(int(new_number))
        else:
            # If the new number has a decimal part, display it with two decimal places
            self.number = "{:.2f}".format(new_number)

        self.number_label.config(text=str(self.number))



class IconButton:
    def __init__(self, master, icon_path, title, bg_color, input_callback):
        self.master = master
        self.bg_color = bg_color
        self.input_callback = input_callback
        self.isSelected = False

        # Load the icon
        self.icon = tk.PhotoImage(file=icon_path)

        # Create a label for the button with the desired background color
        self.button_label = tk.Label(
            master,
            text=title,
            image=self.icon,
            compound=tk.TOP,
            bg=self.bg_color,
            foreground="white",
            bd=0,  # No border
            padx=5,  # Padding between icon and text
            pady=20,
            width=150,
            relief=tk.FLAT
        )
        self.button_label.pack()

        # Bind the click event to the on_button_click method
        self.button_label.bind("<Button-1>", self.on_button_click)

        # Bind the hover event to change the cursor to pointer
        self.button_label.bind("<Enter>", self.on_enter)
        self.button_label.bind("<Leave>", self.on_leave)

    def on_button_click(self, event):
        # Call the common input function with the corresponding case
        self.input_callback(self.button_label.cget("text"))

    def on_enter(self, event):
        # Change the cursor to pointer on hover
        self.button_label.config(bg=primaryBtnSelectedBgColor)

    def on_leave(self, event):
        # Change the cursor back to the default on leave
        if not self.isSelected:
            self.button_label.config(bg=self.bg_color)

    def select(self):
        self.button_label.config(bg=primaryBtnSelectedBgColor)
        self.isSelected = True

    def deselect(self):
        self.button_label.config(bg=primaryBtnBgColor)
        self.isSelected = False


class PrimaryButton:
    def __init__(self, master, text, expand, command, state, side="left"):
        self.master = master

        # Create a button with blue background and white text
        self.button = ttk.Button(
            master,
            text=text,
            command=command,
            state=state,
            style="Primary.TButton"  # Use the correct style name here
        )
        # Pack the button to occupy full width and have padding
        self.button.pack(side=side, fill="both", expand=expand, padx=10, pady=10)

        # Configure the style for the blue button
        master.style = ttk.Style()
        master.style.configure("Primary.TButton", background=primaryBtnSelectedBgColor, foreground="#f7f7f7", padding=(10, 10), borderwidth=0, relief="flat")

        # Disable hover color change
        master.style.map("Primary.TButton", background=[("pressed", primaryBtnSelectedBgColor), ("active", primaryBtnSelectedBgColor)])


class SecondaryButton:
    def __init__(self, master, text, expand, command):
        self.master = master

        # Create a button with blue background and white text
        self.button = ttk.Button(
            master,
            text=text,
            command=command,
            width=60,
            style="Secondary.TButton"  # Use the correct style name here
        )
        # Pack the button to occupy full width and have padding
        self.button.pack(side="top", fill="both", expand=expand, padx=10, pady=10, anchor='w')

        # Configure the style for the blue button
        master.style = ttk.Style()
        master.style.configure("Secondary.TButton", background=secondaryBtnSelectedBgColor, foreground="#f7f7f7", padding=(10, 10), borderwidth=0, relief="flat")

        # Disable hover color change
        master.style.map("Secondary.TButton", background=[("pressed", secondaryBtnSelectedBgColor), ("active", secondaryBtnSelectedBgColor)])


class MetricsticsGUI:
    session_list = []
    minimumCard = None
    maximumCard = None
    meanCard = None
    medianCard = None
    madCard = None
    standardDeviationCard = None
    mode_card = None

    def __init__(self, controller: controller.MainController):
        self.root = tk.Tk()
        self.controller = controller
        # Create a StringVar to store the entered name
        self.sessionName = tk.StringVar()

        def set_dark_theme():
            self.root.style = ttk.Style()
            self.root.style.theme_use('clam')  # You can experiment with different themes
            self.root.style.configure(
                "TLabel", foreground="white", background="#171717", font=("Helvetica", 12)
            )
            self.root.style.configure(
                "TButton", foreground="white", background="#272727", font=("Helvetica", 12)
            )
            self.root.style.configure(
                "TFrame", background="#171717"
            )
            self.root.style.configure(
                "Vertical.TScrollbar", troughcolor='#272727', slidercolor='#007BFF'
            )
        set_dark_theme()
        # set title
        self.root.title("METRISTICS")
        # set window size to full screen
        self.root.state('zoomed')
        
        # set background color
        self.root.configure(background=primaryBgColor)
        
        #---------------------------- header start --------------------------------------------

        # Create the header section
        header_frame = tk.Frame(self.root, height=50, relief="solid", bd=0, bg=primaryBgColor)
        header_frame.pack(fill="x", expand=False)
        header_frame.pack_propagate(False)

        # Add a title label on the left side of the header
        title_label = tk.Label(header_frame, text="METRISTICS", font=("Helvetica", 16), bg=primaryBgColor)
        title_label.pack(side="left", padx=10)

        # Add a close button on the right side of the header
        close_button_icon = tk.PhotoImage(file='icons/close.png')
        # Resize the image to 30x30
        close_button_icon = close_button_icon.subsample(2, 2)

        # Create a Canvas widget and add the image to it
        close_icon_button = tk.Canvas(
            header_frame,
            width=close_button_icon.width(),
            height=close_button_icon.height(),
            bd=0,  # No border
            highlightthickness=0,  # No highlight
            bg=primaryBgColor
        )
        close_icon_button.create_image(0, 0, anchor=tk.NW, image=close_button_icon)

        close_icon_button.pack(side="right", padx=15)

        # Keep a reference to the image to prevent garbage collection
        close_icon_button.image = close_button_icon

        # Bind the event to handle the click action
        close_icon_button.bind("<Button-1>", lambda event: self.root.quit())


        # Bind events to control the button appearance during different states
        def on_enter(event):
            # Change the cursor to pointer on hover
            close_icon_button.config(bg=primaryBgColor)

        close_icon_button.bind("<Enter>", on_enter)

        #---------------------------- header end --------------------------------------------

        #---------------------------- body start --------------------------------------------
        
        # Create three columns with widths 33%, 34%, and 33%
        col1_frame = tk.Frame(self.root, width=self.root.winfo_screenwidth() * 0.33)
        col1_frame.pack(side="left", fill="both", expand=True)

        col2_frame = tk.Frame(self.root, width=self.root.winfo_screenwidth() * 0.34, bg=primaryBgColor)
        col2_frame.pack(side="left", fill="both", expand=True)

        col3_frame = tk.Frame(self.root, width=self.root.winfo_screenwidth() * 0.33, bg=primaryBgColor)
        col3_frame.pack(side="left", fill="both", expand=True)

        #---------------------------- column 1 start -----------------------------------------

        # Add the first row in column 1 with 100% height
        row_frame1 = tk.Frame(col1_frame, bg=primaryBgColor, pady=10)  # Add background color for visibility
        row_frame1.pack(side="top", fill="both")

        def clear_action():
            # Replace this with the action you want the "Clear" button to perform
            print("Clear button clicked!")
            get_user_input('Keyboard')
            self.text_input.delete(1.0, tk.END)
            
            self.minimumCard.update_number(0)
            self.maximumCard.update_number(0)
            self.medianCard.update_number(0)

            self.meanCard.update_number(0)
            self.madCard.update_number(0)
            self.standardDeviationCard.update_number(0)

            self.mode_card.setContent(0)
            self.controller.clear_data()


        def clear_results():
            print("Clearing results!")

            if self.minimumCard:
            
                self.minimumCard.update_number(0)
                self.maximumCard.update_number(0)
                self.medianCard.update_number(0)

                self.meanCard.update_number(0)
                self.madCard.update_number(0)
                self.standardDeviationCard.update_number(0)

                self.mode_card.setContent(0)
                self.controller.clear_data()


        def get_user_input(button_title):
            clear_results()
            # Common function to get user input based on the button clicked
            if button_title == "Keyboard":
                print("Getting keyboard input")
                selected_input_text.config(text="Keyboard Input")
                selected_input_subtext.config(text="Custom user entered data")
                keyboard_button.select()
                file_button.deselect()
                auto_button.deselect()
                # Your keyboard input handling code here
            elif button_title == "File":
                print("Getting file input")
                file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
                if file_path:
                    try:
                        with open(file_path, 'r') as file:
                            content = file.read().strip()
                            numbers = [int(num) for num in content.split(",")]

                            # Set the text area input to the numbers from the file
                            self.text_input.delete(1.0, tk.END)  # Clear existing content
                            self.text_input.insert(tk.END, ", ".join(map(str, numbers)))
                            keyboard_button.deselect()
                            file_button.select()
                            auto_button.deselect()
                            selected_input_text.config(text="File Input")
                            file_size_kb = os.path.getsize(file_path) / 1024  # File size in kilobytes
                            selected_input_subtext.config(text=f"File: {os.path.basename(file_path)} | Size: {file_size_kb:.2f} KB")
                            

                    except ValueError:
                        tk.messagebox.showerror("Error", "Incorrect input found in the uploaded file. File should contain numbers separated by commas.")
                else:
                    print("No file selected.")
            elif button_title == "Auto":
                print("Generating random positive numbers")
                keyboard_button.deselect()
                file_button.deselect()
                auto_button.select()
                selected_input_text.config(text="Auto generated input")
                # Your code to generate random positive numbers (between 300 and 1000) here
                random_numbers = [random.randint(1, 1000) for _ in range(random.randint(0, 1000))]
                sorted_numbers = sorted(random_numbers)
                selected_input_subtext.config(text=f"Generated {len(sorted_numbers)} random numbers")
                print("Generated numbers:", sorted_numbers)

                # Set the text area input to the generated and sorted random numbers
                self.text_input.delete(1.0, tk.END)  # Clear existing content
                self.text_input.insert(tk.END, ", ".join(map(str, sorted_numbers)))


        def get_name():
            name = self.sessionName.get()
            print(f"Entered Name: {name}")
            if name:
                try:
                    self.controller.save_session(name=name)
                    # Sameer - add logic here to refresh list
                except ResultsNotAvailableError as e:
                    print(f"Error: {e}")
                    messagebox.showinfo("Alert", e)
            popup.destroy()  # Close the popup after getting the name


        def open_popup():
            global popup
            popup = tk.Toplevel(self.root)
            popup.title("Session name")

            window_width = 300
            window_height = 230

            # get the screen dimension
            screen_width = popup.winfo_screenwidth()
            screen_height = popup.winfo_screenheight()

            # find the center point
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            # set the position of the window to the center of the screen
            popup.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

            # Create a StringVar to store the entered name
            self.sessionName.set("")  # Clear any previous input

            frame = tk.Frame(popup)
            frame.pack(padx=10, pady=10)

            # Label at the top
            label = tk.Label(frame, text="Enter session name", font=16)
            label.pack(side="top", pady=5)

            # session name input
            # Validate function to enable/disable the "Save" button
            def validate_entry(value):
                if len(value) >= 1:
                    save_button["state"] = "normal"
                else:
                    save_button["state"] = "disabled"
                return True
            
            entry_font = ("Arial", 18)
            name_entry = tk.Entry(frame, textvariable=self.sessionName, font=entry_font, background=primaryBtnBgColor, foreground="white", validate="key", validatecommand=(validate_entry, "%P"))
            name_entry.pack(pady=10, fill="x", padx=10)

            # Button to save
            save_button = PrimaryButton(frame, text="Save", expand=True, command=get_name, state="normal", side="top")

            # Button to cancel
            cancel_button = SecondaryButton(frame, text="Cancel", expand=True, command=popup.destroy)

            # Set focus on the entry widget
            name_entry.focus_set()


        def save_action():
            # Replace this with the action you want the "Clear" button to perform
            print("Save button clicked!")
            open_popup()


        def on_text_area_change(event):
            # Your code to handle the text area change goes here
            print("Text area content changed")
            # switch to custom user input
            get_user_input('Keyboard')

        
        def generate_action():
            # Replace this with the action you want the "Clear" button to perform
            print("Generate button clicked!")
            
            self.input_text = self.text_input.get("1.0", tk.END).strip()

            if not self.input_text:
                messagebox.showinfo("Alert", "Input is empty!")

            # Check if the input_text contains only numbers, spaces, and commas
            elif re.match("^[0-9, ]+$", self.input_text):
                # Perform actions with the input_text as needed
                print("Generate button clicked! Input text:", self.input_text)

                # Split the input_text into an array of numbers
                numbers = [int(num.strip()) for num in self.input_text.split(',')]

                if(len(numbers)<2):
                    messagebox.showinfo("Alert", "Please enter atleast two numbers")

                # Perform actions with the array of numbers as needed
                print("Generate button clicked! Numbers:", numbers)

                result = self.controller.calculate_metrics(numbers)

                print(result)

                self.text_input.delete(1.0, tk.END)
                self.text_input.insert(tk.END, ", ".join(map(str, result["sorted_data"])))

                self.minimumCard.update_number(result["min_value"])
                self.maximumCard.update_number(result["max_value"])
                self.medianCard.update_number(result["median_value"])

                self.meanCard.update_number(result["mean_value"])
                self.madCard.update_number(result["mean_abs_deviation"])
                self.standardDeviationCard.update_number(result["std_deviation"])

                self.mode_card.setContent(", ".join(map(str, result["mode_value"])))


            else:
                # Display an error message or take appropriate action
                print("Invalid input! Please enter numbers, spaces, and commas only.")
                messagebox.showinfo("Alert", "Invalid input! Please enter numbers, spaces, and commas only.")


        # Create three IconButton instances in the first row of column 1
        keyboard_button = IconButton(row_frame1, 'icons/keyboard.png', 'Keyboard', primaryBtnBgColor, get_user_input)
        file_button = IconButton(row_frame1, 'icons/file.png', 'File', primaryBtnBgColor, get_user_input)
        auto_button = IconButton(row_frame1, 'icons/ai.png', 'Auto', primaryBtnBgColor, get_user_input)

        # Pack the buttons in a flex-row fashion with space between them
        keyboard_button.button_label.pack(side="left", padx=10)
        file_button.button_label.pack(side="left", padx=10)
        auto_button.button_label.pack(side="left", padx=10)

        # Add the second row in column 1
        row_frame2 = tk.Frame(col1_frame, bg=primaryBgColor, padx=0, pady=10)  # Add background color for visibility
        row_frame2.pack(side="top", fill="both")

        # Add a frame for the text labels
        frame_text_labels = tk.Frame(row_frame2, bg=primaryBgColor)
        frame_text_labels.pack(side="left", fill="both")

        # Add the first text label on the left of the frame
        selected_input_text = tk.Label(frame_text_labels, text="Your Text Here", fg='white', bg=primaryBgColor)
        selected_input_text.pack(side="top", padx=10, anchor="w")

        # Add the second text label below the existing selected_input_text
        selected_input_subtext = tk.Label(frame_text_labels, text="Another Text Label", fg='white', bg=primaryBgColor)
        selected_input_subtext.pack(side="top", padx=10, anchor="w")

        # Save button
        save_button = PrimaryButton(row_frame2, text="Save", expand=False, command=save_action, state="normal")
        save_button.button.pack(side="right", padx=10, pady=10)

        # select keyboard input by default - can be set only after labels are initialized
        get_user_input('Keyboard')

        # scrollable text area
        # Add a new row frame between row_frame2 and row_frame3
        row_frame_text_input = tk.Frame(col1_frame, bg=primaryBgColor, padx=10, pady=0)  # Add background color for visibility
        row_frame_text_input.pack(side="top", fill="both", expand=True)

        # Add a scrollable textarea input in the new row frame
        self.text_input = tk.Text(row_frame_text_input, wrap="word", width=40, height=10, padx=10, pady=10, background=primaryBgColor, foreground="white")
        self.text_input.pack(side="left", fill="both", expand=True)
        self.text_input.bind("<KeyRelease>", on_text_area_change)

        # Add a scrollbar to the textarea
        text_scrollbar = ttk.Scrollbar(row_frame_text_input, command=self.text_input.yview)
        text_scrollbar.pack(side="right", fill="y")

        # Create a custom style for the scrollbar
        scrollbar_style = ttk.Style()
        scrollbar_style.configure("TScrollbar")

        # Apply the custom style to the scrollbar
        text_scrollbar.config(style="TScrollbar")

        self.text_input.config(yscrollcommand=text_scrollbar.set, highlightbackground=primaryBtnBgColor, highlightcolor=primaryBtnBgColor, insertbackground='white')

        # Add the third row in column 1
        row_frame3 = tk.Frame(col1_frame, bg=primaryBgColor, padx=0, pady=10)  # Add background color for visibility
        row_frame3.pack(side="top", fill="both")

        # Add a clear button on the left side of the third row
        clear_button = PrimaryButton(row_frame3, text="Clear", expand=True, command=clear_action, state="normal")

        generate_button = PrimaryButton(row_frame3, text="Generate", expand=True, command=generate_action, state="normal")

        #------------------------------ column 1 end -----------------------------------------------------------------
        #------------------------------ column 2 start ---------------------------------------------------------------

        # Add a frame for the label cards
        row_frame4 = tk.Frame(col2_frame, bg=primaryBgColor, pady=10, padx=10)  # Add background color for visibility
        row_frame4.pack(side="top", fill="both")

        self.minimumCard = InfoCard(row_frame4, 0, 'Minimum')
        self.minimumCard.grid(row=0, column=0)

        self.maximumCard = InfoCard(row_frame4, 0, 'Maximum')
        self.maximumCard.grid(row=0, column=1)

        self.medianCard = InfoCard(row_frame4, 0, 'Median')
        self.medianCard.grid(row=0, column=2)

        # Add a frame for the label cards
        row_frame5 = tk.Frame(col2_frame, bg=primaryBgColor, pady=10, padx=10)  # Add background color for visibility
        row_frame5.pack(side="top", fill="both")

        self.meanCard = InfoCard(row_frame5, 0, 'Mean')
        self.meanCard.grid(row=1, column=0)
        self.madCard = InfoCard(row_frame5, 0, 'MAD')
        self.madCard.grid(row=1, column=1)
        self.standardDeviationCard = InfoCard(row_frame5, 0, 'Standard Deviation')
        self.standardDeviationCard.grid(row=1, column=2)

        # Add a frame for the label cards
        row_frame6 = tk.Frame(col2_frame, bg=primaryBgColor, pady=10, padx=10)  # Add background color for visibility
        row_frame6.pack(side="top", fill="both")

        # mode
        # Add a frame for the label cards
        mode_frame = tk.Frame(col2_frame, bg=primaryBgColor, padx=10)  # Add background color for visibility
        mode_frame.pack(side="top", fill="both", expand=True)

        self.mode_card = ScrollableLabelFrame(mode_frame, "Mode", "0")
        self.mode_card.frame.pack(fill="both", expand=True, padx=(10, 10), pady=(0, 20))
        
        #------------------------------ column 2 end ------------------------------------------------------------------

        #------------------------------ column 3 start ---------------------------------------------------------------

        # Add a frame for the label cards
        row_frame7 = tk.Frame(col3_frame, bg=primaryBgColor)  # Add background color for visibility
        row_frame7.pack(side="top", fill="x", padx=300, pady=(10, 0))

        row_frame8 = tk.Frame(col3_frame, bg=primaryBgColor, height=self.root.winfo_screenheight() * 0.5)  # Add background color for visibility
        row_frame8.pack(side="top", fill="x", padx=(10, 0))

        scrollable_frame = ScrollableLabelFrame(row_frame8, "", descriptive_statistics_notes)
        scrollable_frame.frame.pack(fill="both", expand=True)

        row_frame8 = tk.Frame(col3_frame, bg=primaryBgColor, height=self.root.winfo_screenheight() * 0.5)  # Add background color for visibility
        row_frame8.pack(side="top", fill="x", padx=(0, 0), pady=10)

        # Add the first text label on the left of the frame
        session_label_text = tk.Label(row_frame8, text="Session(s):", fg='white', bg=primaryBgColor)
        session_label_text.pack(side="top", padx=10, pady= (10, 0), anchor="w")
        
        # Add a scrollbar list box
        row_frame = tk.Frame(col3_frame, background=primaryBgColor, highlightthickness=3, relief="flat", highlightbackground="#272727")
        row_frame.pack(side="top", fill="both", expand=True, padx=(10, 0), pady=(0, 20))

        row_frame9 = tk.Frame(row_frame, bg=primaryBgColor)
        row_frame9.pack(side="top", fill="both", expand=True, padx=(1, 0), pady=5)
        
        self.scrollbar = ttk.Scrollbar(row_frame9)
        self.scrollbar.pack(side="right", fill="y")

        small_font = font.Font(size=14)

        mylist = Listbox(row_frame9, yscrollcommand=self.scrollbar.set, font=small_font, background=primaryBgColor, bg=primaryBgColor, border=0, foreground="white")
        
        def on_item_click(event):
            selected_index = mylist.curselection()
            if selected_index:
                selected_item_id = selected_index[0]
                print(f"Item clicked with ID: {selected_item_id}")

                # Check if the index is within the bounds of the self.session_list
                if 0 <= selected_item_id < len(self.session_list):
                    selected_session = self.session_list[selected_item_id]

                    # Display session name based on id
                    session_name = selected_session.name  # Replace with the actual attribute
                    print(f"Session Name: {session_name}")

                    # Display a confirmation dialog
                    answer = askyesno(
                        title='Confirmation',
                        message=f'Are you sure that you want to load session: {session_name}?'
                    )

                    if answer:
                        print(f"Loading session with id: {selected_item_id}")
                        print(selected_index)
                        result = self.controller.load_session(selected_session.id)

                        print("session: loading file input")
                        file_path = result.datasetFilePath
                        name = result.name
                        timestamp = result.timestamp
                        results = result.results
                        if file_path:
                            try:
                                with open(file_path, 'r') as file:
                                    content = file.read().strip()
                                    numbers = [int(num) for num in content.split(",")]

                                    # Set the text area input to the numbers from the file
                                    self.text_input.delete(1.0, tk.END)  # Clear existing content
                                    self.text_input.insert(tk.END, ", ".join(map(str, numbers)))
                                    keyboard_button.select()
                                    selected_input_text.config(text="Session loaded")
                                    selected_input_subtext.config(text=f"Name: {name} | Date: {format_timestamp(timestamp)} ")
                                    

                            except ValueError:
                                tk.messagebox.showerror("Error", "Incorrect input found in the uploaded file. File should contain numbers separated by commas.")
                        else:
                            print("No file selected.")

                        print(results)

                        self.minimumCard.update_number(results["min"])
                        self.maximumCard.update_number(results["max"])
                        self.medianCard.update_number(results["median"])

                        self.meanCard.update_number(results["mean"])
                        self.madCard.update_number(results["mean_abs_deviation"])
                        self.standardDeviationCard.update_number(results["std_deviation"])

                        self.mode_card.setContent(", ".join(map(str, results["mode"])))

        def format_timestamp(timestamp) -> str:
            if timestamp is not None:
                date_object = datetime.utcfromtimestamp(timestamp)
                formatted_date = date_object.strftime("%d-%b-%Y %H:%M:%S")
                return formatted_date
            return ""

        mylist.bind("<ButtonRelease-1>", on_item_click)

        self.session_list = self.controller.get_all_sessions()
        for item in self.session_list:
            mylist.insert("end", str(item.name) + " " + "(" + format_timestamp(item.timestamp) + ")")

        mylist.pack(side="left", fill="both", anchor='w', expand=True, padx=(10, 0))
        self.scrollbar.config(command=mylist.yview)

        # Create a custom style for the scrollbar
        scrollbar_style = ttk.Style()

        # Apply the custom style to the scrollbar
        scrollbar_style.configure('TScrollbar', troughcolor='gray', background='#f7f7f7', thickness=12)



        #------------------------------ column 3 end ------------------------------------------------------------------

    def run(self):
        self.root.mainloop()