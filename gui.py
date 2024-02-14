# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Rectangle Area")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Width:"
    lbl_width = Label(frm_main, text="Width:")

    # Create an integer entry box where the user will enter her age.
    ent_width = IntEntry(frm_main)

    # Create a label that displays "inches"
    lbl_width_units = Label(frm_main, text="inches")

        # Create a label that displays "Height:"
    lbl_height = Label(frm_main, text="Height:")

    # Create an integer entry box where the user will enter her age.
    ent_height = IntEntry(frm_main)

    # Create a label that displays "inches"
    lbl_height_units = Label(frm_main, text="inches")

    # Create labels that will display the results.
    lbl_area = Label(frm_main, width=5)
    lbl_area_units = Label(frm_main, text="squared inches")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Create status bar
    lbl_statusbar = Label(frm_main, width=10)

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_width.grid(      row=0, column=0, padx=3, pady=3)
    ent_width.grid(      row=0, column=1, padx=3, pady=3)
    lbl_width_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_height.grid(      row=1, column=0, padx=3, pady=3)
    ent_height.grid(      row=1, column=1, padx=3, pady=3)
    lbl_height_units.grid(row=1, column=2, padx=0, pady=3)

    lbl_area.grid(      row=2, column=2, padx=(30,3), pady=3)
    lbl_area_units.grid(row=2, column=3, padx=0, pady=3)

    btn_clear.grid(row=3, column=0, padx=3, pady=3, columnspan=4, sticky="w")
    lbl_statusbar.grid(row=4, column=0, padx=0, pady=3)

    # This function will be called each time
    # the user presses the "Clear" button.

    def calculate(event):
        try:
            width = ent_width.get()
            height = ent_height.get()
            if width!=0 and height!=0:
                area = width * height
                lbl_area.config(text=f"{area:.0f}")
            else:
                 lbl_statusbar.config(text="Invalid input")
        except:
            lbl_area.config(text="")
            lbl_statusbar.config(text="")

    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_width.clear()
        ent_height.clear()
        lbl_statusbar.config(text="")
        lbl_area.config(text="")
        ent_width.focus()
        ent_height.focus()


    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_height.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_width.focus()
    ent_height.focus()

# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
