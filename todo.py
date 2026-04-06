import tkinter as tk
from tkinter import messagebox
import os

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    return []

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = entry.get()
    if task != "":
        tasks.append("[ ] " + task)
        update_listbox()
        save_tasks()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task")

def mark_complete():
    try:
        selected = listbox.curselection()[0]
        tasks[selected] = tasks[selected].replace("[ ]", "[✔]")
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task")

def clear_all():
    confirm = messagebox.askyesno("Confirm", "Delete all tasks?")
    if confirm:
        tasks.clear()
        update_listbox()
        save_tasks()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

root = tk.Tk()
root.title("To-Do List App")
root.geometry("450x550")
root.configure(bg="#1e1e2f")

tasks = load_tasks()

header = tk.Label(root, text="My To-Do App", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white")
header.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add", width=10, bg="#4CAF50", fg="white", command=add_task)
add_btn.grid(row=0, column=0, padx=5, pady=5)

delete_btn = tk.Button(btn_frame, text="Delete", width=10, bg="#f44336", fg="white", command=delete_task)
delete_btn.grid(row=0, column=1, padx=5, pady=5)

complete_btn = tk.Button(btn_frame, text="Complete", width=10, bg="#2196F3", fg="white", command=mark_complete)
complete_btn.grid(row=1, column=0, padx=5, pady=5)

clear_btn = tk.Button(btn_frame, text="Clear All", width=10, bg="#ff9800", fg="white", command=clear_all)
clear_btn.grid(row=1, column=1, padx=5, pady=5)

frame = tk.Frame(root)
frame.pack(pady=20)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, width=40, height=15, font=("Arial", 11), yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT)

scrollbar.config(command=listbox.yview)

update_listbox()

footer = tk.Label(root, text="Built with Python Tkinter", bg="#1e1e2f", fg="gray")
footer.pack(pady=10)

root.mainloop()
