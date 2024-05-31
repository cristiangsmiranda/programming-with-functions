import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry  

def main():
    root = tk.Tk()

    frm_main = Frame(root)
    frm_main.master.title("Rectangle Area")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    populate_main_window(frm_main)

    root.mainloop()

def populate_main_window(frm_main):
    lbl_width = Label(frm_main, text="Enter the width (10-200): ")
    lbl_length = Label(frm_main, text="Enter the length (20-90): ")
    lbl_rectangle = Label(frm_main, text="Area of rectangle:")

    ent_width = IntEntry(frm_main, width=5, lower_bound=10, upper_bound=200)
    ent_length = IntEntry(frm_main, width=5, lower_bound=20, upper_bound=90)

    txt_rectangle = Label(frm_main, width=10, anchor="e")
    lbl_width_units = Label(frm_main, text="millimeters")
    lbl_length_units = Label(frm_main, text="millimeters")
    lbl_rectangle_units = Label(frm_main, text="square millimeters")

    btn_clear = Button(frm_main, text="Clear")

    lbl_width.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
    ent_width.grid(      row=0, column=1, padx=3, pady=2, sticky="w")
    lbl_width_units.grid(row=0, column=2, padx=0, pady=2, sticky="w")

    lbl_length.grid(      row=1, column=0, padx=3, pady=2, sticky="e")
    ent_length.grid(      row=1, column=1, padx=3, pady=2, sticky="w")
    lbl_length_units.grid(row=1, column=2, padx=0, pady=2, sticky="w")

    lbl_rectangle.grid(   row=2, column=0, padx=3, pady=2, sticky="e")
    txt_rectangle.grid(   row=2, column=1, padx=3, pady=2, sticky="w")
    lbl_rectangle_units.grid(row=2, column=2, padx=0, pady=2, sticky="w")

    btn_clear.grid(    row=3, column=0, columnspan=3, padx=3, pady=2)

    def calculate(event=None):
        try:
            width = ent_width.get()
            length = ent_length.get()
            rectangle = width * length
            txt_rectangle.config(text=f"{rectangle:.2f}")
        except ValueError:
            txt_rectangle.config(text="")

    def clear():
        btn_clear.focus()
        ent_width.clear()
        ent_length.clear()
        txt_rectangle.config(text="")
        ent_width.focus()

    ent_width.bind("<KeyRelease>", calculate)
    ent_length.bind("<KeyRelease>", calculate)
    btn_clear.config(command=clear)
    ent_width.focus()

if __name__ == "__main__":
    main()
