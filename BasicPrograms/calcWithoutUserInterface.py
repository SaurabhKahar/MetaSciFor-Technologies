import tkinter as tk

window = tk.Tk()
window.title("Calculator")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
    
labelNum1 = tk.Label(window, text=f"1st Number: {num1}", bg="blue")
labelNum1.pack()
labelNum2 = tk.Label(window, text=f"2nd Number: {num2}", bg="blue")
labelNum2.pack()

labelOutput = tk.Label(window, text="Result is: ", bg="red")
labelOutput.pack()


def add():
    result = num1 + num2
    labelOutput.config(text = f"Result is: {result}")

def sub():
    result = num1 - num2
    labelOutput.config(text = f"Result is: {result}")

def mul():
    result = num1 * num2
    labelOutput.config(text = f"Result is: {result}")

def div():
    result = num1 / num2
    labelOutput.config(text = f"Result is: {result}")


buttonAdd = tk.Button(window, text="ADD", command=add)
buttonAdd.pack()

buttonSub = tk.Button(window, text="Sub", command=sub)
buttonSub.pack()

buttonMul = tk.Button(window, text="MUL", command=mul)
buttonMul.pack()

buttonDiv = tk.Button(window, text="DIV", command=div)
buttonDiv.pack()


window.mainloop()
    
