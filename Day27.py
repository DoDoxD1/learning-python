from tkinter import *


def button_clicked():
    # my_label.config(text=text.get())
    miles = int(miles_input.get())
    km = miles*1.60934
    output_label.config(text="%.2f" % km)


window = Tk()
window.title("Hello World")
window.config(padx=20, pady=20)

# Learning tkinter
# my_label = tkinter.Label(text="I am a label", font=("Times New Roman", 24, "normal"))
# my_label.grid(column=0, row=0)
#
# # my_label["text"] = "Lol"
# # my_label.config(text="lol")
#
# my_button = tkinter.Button(text="Click me", command=button_clicked)
# my_button.grid(column=1, row=1)
#
# my_button2 = tkinter.Button(text="Click me2", command=button_clicked)
# my_button2.grid(column=2, row=0)
#
# text = tkinter.Entry(width=10)
# text.grid(column=3, row=3)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

output_label = Label(text="0")
output_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=3)

window.mainloop()
