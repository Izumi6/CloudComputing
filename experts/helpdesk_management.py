# Expert System 3: Help Desk Management
# pip install tk (comes pre-installed with Python)

from tkinter import *

def solve_issue():
    if internet_var.get() == 1:
        result.set("Contact Administrator")
    else:
        result.set("Restart Router")

root = Tk()
root.title("Help Desk Expert System")
root.geometry("400x250")

internet_var = IntVar()
result = StringVar()

Label(root, text="Help Desk Expert System", font=("Arial", 14)).pack(pady=10)
Checkbutton(root, text="Internet Issue", variable=internet_var).pack()
Button(root, text="Solve Issue", command=solve_issue).pack(pady=10)
Label(root, textvariable=result, fg="blue").pack()

root.mainloop()
