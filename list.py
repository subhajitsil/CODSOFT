import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x300")
        self.root.configure(bg="#F0F0F0")  # Set background color

        self.tasks = []

        # Task Entry
        self.task_entry = tk.Entry(root, width=30, font=("Arial", 14))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.add_button.grid(row=1, column=0, pady=5, padx=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, font=("Arial", 12), bg="#FF5733", fg="white")
        self.remove_button.grid(row=1, column=1, pady=5, padx=5)

        self.show_button = tk.Button(root, text="Show Tasks", command=self.show_tasks, font=("Arial", 12), bg="#2196F3", fg="white")
        self.show_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            messagebox.showinfo("Task Added", f"Task '{task}' added successfully.")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def remove_task(self):
        selected_task = simpledialog.askstring("Remove Task", "Enter task to remove:")
        if selected_task:
            if selected_task in self.tasks:
                self.tasks.remove(selected_task)
                messagebox.showinfo("Task Removed", f"Task '{selected_task}' removed successfully.")
            else:
                messagebox.showwarning("Task Not Found", f"Task '{selected_task}' not found.")
        else:
            messagebox.showwarning("Empty Input", "Please enter a task.")

    def show_tasks(self):
        if not self.tasks:
            messagebox.showinfo("No Tasks", "No tasks in the to-do list.")
        else:
            tasks_str = "\n".join(self.tasks)
            messagebox.showinfo("To-Do List", tasks_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
