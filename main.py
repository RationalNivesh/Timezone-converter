import time
import tkinter as tk
import pytz
from datetime import datetime

source_time = datetime.now()
timezone = input("What is your timezone? ")
source_timezone = pytz.timezone(timezone)


def clock():
    local_time = datetime.now(source_timezone).strftime(" %H:%M:%S")
    clock_label.config(text=local_time)
    clock_label.after(1000, clock)
window = tk.Tk()
window.title('Clock')
message_1 = tk.Label(window, font=("Arial", 50, "italic"), text="current time", fg="blue")

message = tk.Label(window, font=("Arial", 100, "italic"), text="Converted Time", fg="red")
message.grid(row=0, column=0)

clock_label = tk.Label(window, font=("Arial", 150, "bold"), fg="dark blue")
clock_label.grid(row=1, column=0)

clock()  # Call the clock function to start updating the time
window.mainloop()
