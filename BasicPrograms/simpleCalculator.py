import tkinter as tk
from math import sin, cos, tan, log10, radians, pi

class Calc:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")
        self.expression = ""
        self.result_shown = False
        
        self.root.configure(background='green')
        
        self.entry = tk.Entry(self.root, font=("Arial", 18), bd=10, insertwidth=2, width=25, borderwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        
        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            ('AC', 1, 0), ('+', 1, 1), ('-', 1, 2), ('*', 1, 3),
            ('cos', 2, 0), ('sin', 2, 1), ('tan', 2, 2), ('log', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('/', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('x^2', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('x^3', 5, 3),
            ('%', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3)
        ]
        
        for (text, row, col) in button_texts:
            self.create_button(text, row, col)
        
    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 18), bg='red', fg='white',
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
        
        self.root.grid_rowconfigure(row, weight=1)
        self.root.grid_columnconfigure(col, weight=1)
        
    def on_button_click(self, char):
        if char == 'AC':
            self.expression = ""
        elif char == '=':
            try:
                # Evaluate the expression with math functions and radians conversion
                self.expression = str(eval(self.parse_expression(self.expression)))
                self.result_shown = True
            except Exception as e:
                self.expression = "Error"
        else:
            if self.result_shown:
                self.expression = ""
                self.result_shown = False
            self.expression += str(char)
        
        self.update_entry()
        
    def parse_expression(self, expression):
        # Replace the functions with appropriate math module functions
        expression = expression.replace('sin', 'sin(radians(')
        expression = expression.replace('cos', 'cos(radians(')
        expression = expression.replace('tan', 'tan(radians(')
        expression = expression.replace('log', 'log10(')
        
        expression = expression.replace('x^2', '**2')
        expression = expression.replace('x^3', '**3')
        
        # Closing all opened brackets for trigonometric functions
        for func in ['sin(radians(', 'cos(radians(', 'tan(radians(', 'log10(']:
            count = expression.count(func)
            expression += ')' * count
        
        return expression
        
    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calc(root)
    root.mainloop()
