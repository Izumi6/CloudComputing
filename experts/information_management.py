# Expert System 1: Information Management
# pip install tk (comes pre-installed with Python)

from tkinter import *

def check_security():
    if password_var.get() == 1:
        result.set("Data is Secure")
    else:
        result.set("Weak Password")

root = Tk()
root.title("Information Management System")
root.geometry("400x250")

password_var = IntVar()
result = StringVar()

Label(root, text="Information Management Expert System", font=("Arial", 14)).pack(pady=10)
Checkbutton(root, text="Strong Password", variable=password_var).pack()
Button(root, text="Check", command=check_security).pack(pady=10)
Label(root, textvariable=result, fg="blue").pack()

root.mainloop()
