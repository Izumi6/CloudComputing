# Expert System 4: Employee Performance Evaluation
# pip install tk (comes pre-installed with Python)

from tkinter import *

def evaluate():
    score = int(entry.get())
    if score >= 75:
        result.set("Excellent Performance")
    elif score >= 50:
        result.set("Good Performance")
    else:
        result.set("Needs Improvement")

root = Tk()
root.title("Employee Evaluation Expert System")
root.geometry("400x250")

result = StringVar()

Label(root, text="Employee Evaluation Expert System", font=("Arial", 14)).pack(pady=10)
Label(root, text="Enter Score:").pack()
entry = Entry(root)
entry.pack()
Button(root, text="Evaluate", command=evaluate).pack(pady=10)
Label(root, textvariable=result, fg="blue").pack()

root.mainloop()
