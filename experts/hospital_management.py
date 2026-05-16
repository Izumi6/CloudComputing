# Expert System 2: Hospital and Medical Facilities
# pip install tk (comes pre-installed with Python)

from tkinter import *

def check_disease():
    fever = fever_var.get()
    cough = cough_var.get()
    if fever == 1 and cough == 1:
        result.set("You may have infection. Visit doctor.")
    elif fever == 1:
        result.set("Take rest and medicines.")
    else:
        result.set("You are healthy.")

root = Tk()
root.title("Hospital Expert System")
root.geometry("400x300")

fever_var = IntVar()
cough_var = IntVar()
result = StringVar()

Label(root, text="Hospital Expert System", font=("Arial", 14)).pack(pady=10)
Checkbutton(root, text="Fever", variable=fever_var).pack()
Checkbutton(root, text="Cough", variable=cough_var).pack()
Button(root, text="Check Disease", command=check_disease).pack(pady=10)
Label(root, textvariable=result, fg="blue").pack()

root.mainloop()
