from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title("Clock")

def present_time():
    display_time = time.strftime("%I:%M:%S %p")
    digital_clock.config(text=display_time)
    digital_clock.after(200,present_time)


digital_clock = Label(root,font=("times new roman",150),bg="pink",fg="black")
digital_clock.pack()

present_time()

root.mainloop()
