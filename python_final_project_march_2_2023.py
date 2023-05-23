import datetime
import time
import tkinter as tk


# Create a tkinter window
window = tk.Tk()
window.title("Gifted Gabber Alarm Clock")

# Set the window size
window.geometry("400x400")

# Create a label for the current time
time_label = tk.Label(window, font=("Arial", 50))
time_label.pack()

# Create an entry box for setting the alarm time
alarm_entry = tk.Entry(window, font=("Arial", 20))
alarm_entry.pack(pady=20)

# Create a function to get the current time and update the label
def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Create a function to check if the alarm should go off
def check_alarm():
    alarm_time = alarm_entry.get()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if alarm_time == current_time:
        print("Wakey Wakey eggs and bakey!")
    window.after(1000, check_alarm)

# Call the update_time and check_alarm functions
update_time()
check_alarm()

# Start the tkinter main loop
window.mainloop()