from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Entry
miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

#Label
miles_label = Label(text="Miles", font=("Arial", 16))
miles_label.grid(column=2, row=0)

#Result Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label =Label(text="Km")
kilometer_label.grid(column=2, row=1)

#Button
button = Button(text="Calculate", )
button.grid(column=1, row=2)




window.mainloop()