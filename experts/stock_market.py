# Expert System 5: Stock Market Trading
# pip install tk (comes pre-installed with Python)

from tkinter import *

def market_decision():
    if market_var.get() == 1:
        result.set("Suggestion: Buy Stocks")
    else:
        result.set("Suggestion: Sell or Hold")

root = Tk()
root.title("Stock Market Expert System")
root.geometry("400x250")

market_var = IntVar()
result = StringVar()

Label(root, text="Stock Market Expert System", font=("Arial", 14)).pack(pady=10)
Checkbutton(root, text="Market is Up", variable=market_var).pack()
Button(root, text="Get Suggestion", command=market_decision).pack(pady=10)
Label(root, textvariable=result, fg="blue").pack()

root.mainloop()
