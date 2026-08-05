import tkinter as tk
from tkinter import messagebox, ttk
import os

DATA_FILE = "task.txt"

def add_task():
    task = entry_task.get()
    if task:
        listbox.insert(tk.END, task)
        entry_task.delete(0, tk.END)


def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(0, tk.END)


def delete_all():
    listbox.delete(0, tk.END)


def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task+"\n")


def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                task = line.strip()
                if task:
                    listbox.insert(tk.END, task)

# ---------- ساخت پنجره اصلی ----------
root = tk.Tk()
root.title("مدیریت وظایف - To Do List")
root.geometry("500x500")
root.resizable(False, False)

# ---------- ورودی ----------
frame_top = tk.Frame(root)
frame_top.pack(pady=15)

tk.Label(frame_top, text="وظیفه جدید:", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
entry_task = tk.Entry(frame_top, width=35, font=("Arial", 11))
entry_task.pack(side=tk.LEFT, padx=5)
btn_add = tk.Button(frame_top, text="افزودن", bg="#4caf50", fg="white", command=add_task)
btn_add.pack(side=tk.LEFT, padx=5)

# ---------- لیست وظایف ----------
frame_middle = tk.Frame(root)
frame_middle.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

listbox = tk.Listbox(frame_middle, height=15, font=("Arial", 11), selectbackground="#a6a6a6")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_middle, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# ---------- دکمه‌ها ----------
frame_button = tk.Frame(root)
frame_button.pack(pady=15)

btn_delete = tk.Button(frame_button, text="حذف انتخاب شده", bg="red", fg="white", width=18, command=delete_task)
btn_delete.pack(side=tk.LEFT, padx=10)

btn_clear = tk.Button(frame_button, text="حذف همه", bg="orange", fg="white", width=18, command=delete_all)
btn_clear.pack(side=tk.LEFT, padx=10)


load_tasks()

root.protocol("WM_DELETE_WINDOW", lambda:(save_tasks(), root.destroy()))

root.mainloop()