import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime, timedelta

# Create root window
root = tk.Tk()
root.configure(bg="white")
root.title("Todo Helper")
root.geometry("450x500")

# Dictionary to store tasks and their associated dates
tasks = {}

# Function to update the listbox with color-coded tasks
def update_listbox():
    clear_listbox()
    today = datetime.today()
    for task, date in tasks.items():
        try:
            due_date = datetime.strptime(date, "%Y-%m-%d")
            delta = (due_date - today).days

            if delta < 0:
                color = "red"  # Overdue
            elif delta <= 3:
                color = "yellow"  # Due soon
            else:
                color = "green"  # Distant due date

            lb_tasks.insert("end", f"{task} (Due: {date})")
            lb_tasks.itemconfig("end", fg=color)
        except ValueError:
            messagebox.showerror("Invalid Date", f"Invalid date format for task '{task}'.")

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task(event=None):
    task = txt_task.get()
    date = txt_date.get()
    if task and date:
        try:
            datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            tasks[task] = date
            update_listbox()
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format.")
    else:
        messagebox.showwarning("Incomplete Input", "Please enter both a task and a date.")
    txt_task.delete(0, "end")
    txt_date.delete(0, "end")

def delete_task():
    selected = lb_tasks.get("active")
    if selected:
        task = selected.split(" (Due:")[0]
        if task in tasks:
            confirm = messagebox.askyesno("Confirm Deletion", f"Delete task: '{task}'?")
            if confirm:
                del tasks[task]
                update_listbox()
    else:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

def delete_all():
    confirm = messagebox.askyesno("Delete All", "Are you sure you want to delete all tasks?")
    if confirm:
        tasks.clear()
        update_listbox()

def sort_by_date():
    global tasks
    tasks = dict(sorted(tasks.items(), key=lambda item: item[1]))
    update_listbox()

def random_task():
    if tasks:
        task = random.choice(list(tasks.items()))
        lbl_display["text"] = f"Random Task: {task[0]} (Due: {task[1]})"
    else:
        lbl_display["text"] = "No tasks available!"

def exit_program():
    root.quit()

# GUI Elements
lbl_title = tk.Label(root, text="To-Do List with Dates", bg="white", font=("Arial", 14))
lbl_title.grid(row=0, column=0, columnspan=2, pady=10)

lbl_display = tk.Label(root, text="", bg="white", fg="blue")
lbl_display.grid(row=1, column=0, columnspan=2)

lbl_task = tk.Label(root, text="Task:", bg="white")
lbl_task.grid(row=2, column=0, pady=5, sticky="e")

txt_task = tk.Entry(root, width=30)
txt_task.grid(row=2, column=1, pady=5)

lbl_date = tk.Label(root, text="Due Date (YYYY-MM-DD):", bg="white")
lbl_date.grid(row=3, column=0, pady=5, sticky="e")

txt_date = tk.Entry(root, width=30)
txt_date.grid(row=3, column=1, pady=5)

btn_add_task = tk.Button(root, text="Add Task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row=4, column=0, pady=5)

btn_delete_task = tk.Button(root, text="Delete Task", fg="green", bg="white", command=delete_task)
btn_delete_task.grid(row=5, column=0, pady=5)

btn_delete_all = tk.Button(root, text="Delete All", fg="green", bg="white", command=delete_all)
btn_delete_all.grid(row=6, column=0, pady=5)

btn_sort_date = tk.Button(root, text="Sort by Date", fg="green", bg="white", command=sort_by_date)
btn_sort_date.grid(row=7, column=0, pady=5)

btn_random_task = tk.Button(root, text="Random Task", fg="green", bg="white", command=random_task)
btn_random_task.grid(row=8, column=0, pady=5)

btn_exit = tk.Button(root, text="Exit", fg="green", bg="white", command=exit_program)
btn_exit.grid(row=9, column=0, pady=5)

lb_tasks = tk.Listbox(root, width=50, height=10)
lb_tasks.grid(row=4, column=1, rowspan=6, padx=10)

# Populate listbox at program start
update_listbox()

# Start the main loop
root.mainloop()
