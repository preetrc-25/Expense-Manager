# main.py
import tkinter as tk
from tkinter import ttk
import db
from transactions import TransWindow
from categories import CatWindow

class App(tk.Tk):
    def __init__(self):
        super().__init__(); self.title("Expense Manager (Minimal)"); self.geometry("300x200")
        self.build()

    def build(self):
        f = ttk.Frame(self, padding=20); f.pack(fill="both", expand=True)
        ttk.Button(f, text="Transactions", command=lambda: TransWindow(self)).pack(fill="x", pady=5)
        ttk.Button(f, text="Categories", command=lambda: CatWindow(self)).pack(fill="x", pady=5)
        ttk.Button(f, text="Quit", command=self.destroy).pack(fill="x", pady=5)

if __name__ == "__main__":
    db.init_db()
    App().mainloop()
