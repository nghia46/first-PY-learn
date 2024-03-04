import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def complete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task, {'bg': 'light green'})
def undo_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task,{'bg': ''})
        
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

root = tk.Tk()
root.title("To-Do List App")

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(root, text="Undo Task", command=undo_task)
complete_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.RIGHT, padx=5)

root.mainloop()
