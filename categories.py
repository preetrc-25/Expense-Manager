# categories.py
import tkinter as tk
from tkinter import ttk
import db

class CatWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master); self.title("Categories"); self.geometry("300x200")
        self.build(); self.refresh()

    def build(self):
        f = ttk.Frame(self, padding=8); f.pack(fill="both", expand=True)
        row = ttk.Frame(f); row.pack(fill="x")
        ttk.Label(row, text="New:").pack(side="left")
        self.n = tk.StringVar(); ttk.Entry(row, textvariable=self.n).pack(side="left")
        ttk.Button(row, text="Add", command=self.add).pack(side="left")
        self.listbox = tk.Listbox(f); self.listbox.pack(fill="both", expand=True, pady=6)

    def add(self):
        name = self.n.get().strip()
        if name:
            db.add_category(name); self.n.set(""); self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for c in db.get_categories(): self.listbox.insert(tk.END, c)
