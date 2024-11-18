from tkinter import *

def miles_to_kilo():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")

window= Tk()
window.title('Miles to kilometer converter')
window.minsize(width=200, height=100)
window.config(padx=30, pady=30)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equale to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="o")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_kilo)
calculate_button.grid(column=1, row=2)


window.mainloop()

