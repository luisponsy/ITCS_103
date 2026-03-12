import tkinter as tk
def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    result_label.config(text=f"The sum of {num1} + {num2} is {result}")

def subtract():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 - num2
    result_label.config(text=f"The difference between{num1} - {num2} is {result}")

def multiply():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 * num2
    result_label.config(text=f"The product of {num1} * {num2} is {result}")

def divide():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 / num2
    result_label.config(text=f"The quotient of {num1} / {num2} is {result}")

window = tk.Tk()
window.title("Simple Calculator")

window.configure(bg="lightblue")
frame = tk.Frame(window,bg="lightblue", padx=10,pady=10)
frame.grid(row=0,column=0)

result_label = tk.Label (frame,text="Enter numbers then choose operation")
result_label.grid(row=0,column=0,columnspan=2,pady=5)

label1 = tk.Label(frame, text="Enter 1st Number:")
label1.grid(row=1,column=0)

entry1 = tk.Entry(frame)
entry1.grid(row=1, column=1)

label2 = tk.Label(frame, text="Enter 2nd Number:")
label2.grid(row=2,column=0)

entry2 = tk.Entry(frame)
entry2.grid(row=2,column=1)

btn_add = tk.Button(frame, text="Add",width=10, command=add)
btn_add.grid(row=3,column=0,pady=5)

btn_add = tk.Button(frame, text="Subtract",width=10, command=subtract)
btn_add.grid(row=4,column=0,pady=5)

btn_add = tk.Button(frame, text="Multiply",width=10, command=multiply)
btn_add.grid(row=3,column=1,pady=5)

btn_add = tk.Button(frame, text="Divide",width=10, command=divide)
btn_add.grid(row=4,column=1,pady=5)
window.mainloop()