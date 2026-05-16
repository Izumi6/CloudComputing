# Expert System 6: Airline Scheduling and Cargo
# pip install tk (comes pre-installed with Python)

from tkinter import *

def flight_status():
    if weather_var.get() == 1:
        result.set("Flight Can Be Scheduled")
    else:
        result.set("Delay Flight")

root = Tk()
root.title("Airline Management Expert System")
root.geometry("400x250")

weather_var = IntVar()
result = StringVar()

Label(root, text="Airline Management Expert System", font=("Arial", 14)).pack(pady=10)
Checkbutton(root, text="Clear Weather", variable=weather_var).pack()
Button(root, text="Check Status", command=flight_status).pack(pady=10)
Label(root, textvariable=result, fg="blue").pack()

root.mainloop()
