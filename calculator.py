import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x450")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(
            self.root, font=("Arial", 24), bd=10, relief=tk.RIDGE,
            justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=10, ipady=10, sticky="nsew")

        # Create a dictionary to map button text to their positions
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(
                self.root, text=text, font=("Arial", 20), width=5, height=2,
                relief=tk.RAISED, bd=2
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            btn.bind("<Button-1>", self.on_click)

        # Configure grid weights for responsive resizing
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

        # Bind keyboard keys
        self.root.bind("<Key>", self.on_key_press)

    def on_click(self, event):
        text = event.widget.cget("text")
        self.handle_input(text)

    def on_key_press(self, event):
        key = event.keysym
        char = event.char

        if key == "Return":
            self.handle_input("=")
        elif key == "BackSpace":
            self.entry.delete(len(self.entry.get())-1, tk.END)
        elif key in ("Escape", "Delete"):
            self.handle_input("C")
        elif char in "0123456789+-*/":
            self.handle_input(char)

    def handle_input(self, value):
        if value == "=":
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == "C":
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, value)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
