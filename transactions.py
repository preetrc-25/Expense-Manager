# transactions.py
import tkinter as tk
from tkinter import ttk, messagebox
import db

class TransWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master); self.title("Transactions"); self.geometry("520x350")
        self.build(); self.refresh()

    def build(self):
        frm = ttk.Frame(self, padding=8); frm.pack(fill="both", expand=True)

        row = ttk.Frame(frm); row.pack(fill="x")
        ttk.Label(row, text="Date:").grid(row=0,column=0); self.date = tk.StringVar()
        ttk.Entry(row, textvariable=self.date, width=12).grid(row=0,column=1)
        ttk.Label(row, text="Amt:").grid(row=0,column=2); self.amt = tk.StringVar()
        ttk.Entry(row, textvariable=self.amt, width=8).grid(row=0,column=3)
        ttk.Label(row, text="Cat:").grid(row=0,column=4); self.cat = tk.StringVar()
        self.cat_cb = ttk.Combobox(row, textvariable=self.cat, width=12); self.cat_cb.grid(row=0,column=5)
        self.kind = tk.StringVar(value="Expense")
        ttk.Radiobutton(row, text="Exp", variable=self.kind, value="Expense").grid(row=1,column=1)
        ttk.Radiobutton(row, text="Inc", variable=self.kind, value="Income").grid(row=1,column=2)
        ttk.Button(row, text="Add", command=self.add).grid(row=1,column=5)

        self.tree = ttk.Treeview(frm, columns=("id","date","desc","cat","kind","amt"), show="headings")
        for h in ("id","date","desc","cat","kind","amt"): self.tree.heading(h,text=h)
        self.tree.pack(fill="both", expand=True, pady=6)

        btns = ttk.Frame(frm); btns.pack(fill="x")
        ttk.Button(btns, text="Delete", command=self.delete).pack(side="left")
        ttk.Button(btns, text="Refresh", command=self.refresh).pack(side="left")

    def add(self):
        date = self.date.get() or "today"
        try: amount = float(self.amt.get())
        except: messagebox.showerror("Err","Amount number"); return
        cat = self.cat.get() or "Other"
        db.add_category(cat)
        db.add_tx(date, "", amount, cat, self.kind.get())
        self.amt.set(""); self.refresh()

    def refresh(self):
        self.cat_cb['values'] = db.get_categories() or ["Other"]
        for r in self.tree.get_children(): self.tree.delete(r)
        for t in db.get_txs(): self.tree.insert("", "end", values=(t["id"], t["date"], t["desc"], t["category"], t["kind"], t["amount"]))

    def delete(self):
        sel = self.tree.selection()
        if not sel: return
        txid = self.tree.item(sel[0])['values'][0]
        db.delete_tx(txid); self.refresh()
