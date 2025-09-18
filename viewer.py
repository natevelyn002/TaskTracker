import tkinter as tk
import json
import os

# TK_SILENCE_DEPRECATION=1 python viewer.py
# python viewer.py

task_file = "tasks.json"
if os.path.exists(task_file):
    with open("tasks.json", 'r') as f:
        tasks = json.load(f)

def status_type(canvas, x , y, status):
    radius = 8
    if status == "todo":
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="grey", width = 1 )
    elif status == "in-progress":
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="grey", width = 1)
        canvas.create_arc(x - radius, y - radius, x + radius, y + radius, start=90, extent=180, fill="grey", outline="grey")
    elif status == "done":
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="grey", fill="green", width = 2)
    else:
        raise ValueError("Unknown status type")
    
root = tk.Tk()
root.title("Task Viewer")

def refresh_tasks():
    # Remove old widgets/widgets from prior run
    for widget in root.winfo_children():
        widget.destroy()
    with open("tasks.json", 'r') as f:
        tasks = json.load(f)
    for task in tasks:
        frame = tk.Frame(root)
        frame.pack(anchor='w')
        canvas = tk.Canvas(frame, width=20, height=20)
        canvas.pack(side='left')
        status_type(canvas, 11, 11, task['status'])
        label = tk.Label(frame, text=task['description'])
        label.pack(side='left')
    root.after(2000, refresh_tasks)  # refresh every 2 seconds


refresh_tasks()
root.mainloop()
