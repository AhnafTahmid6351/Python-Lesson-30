from tkinter import *
from tkinter import messagebox

tasks = ["Do Homework", "Have a Snack", "Read for 20 Minutes", "Pack School Bag", "Get Ready for Bed"]
current_task_index = 0

def handle_keypress(event):
    if event.char:
        char_label.config(text=f"Last typed character: '{event.char}'")

def handle_click(event):
    status_label.config(text="Routine area clicked!")

def show_next_task():
    global current_task_index
    user_task = task_entry.get().strip()
    
    if not user_task:
        messagebox.showwarning("Warning", "No task entered! Please enter a task name before proceeding.")
        return
    
    if current_task_index < len(tasks):
        next_task = tasks[current_task_index]
        current_task_index += 1
        output_label.config(text=f"Entered Task: {user_task}\nNext Task in Routine: {next_task}")
    else:
        output_label.config(text="All routine tasks completed for today!")

window = Tk()
window.title("After-School Routine Checker")
window.geometry("450x420")

title_label = Label(window, text="After-School Routine Checker", font=("Helvetica", 14, "bold"))
title_label.pack(pady=10)

instruction_label = Label(window, text="Enter your task:")
instruction_label.pack(pady=5)

task_entry = Entry(window, width=30)
task_entry.pack(pady=5)
task_entry.bind("<Key>", handle_keypress)

char_label = Label(window, text="Last typed character: None", fg="blue")
char_label.pack(pady=5)

routine_area = Label(window, text="[ Click inside this Routine Area ]", bg="lightgrey", width=35, height=3, relief=GROOVE)
routine_area.pack(pady=10)
routine_area.bind("<Button-1>", handle_click)

status_label = Label(window, text="", fg="green")
status_label.pack(pady=2)

action_button = Button(window, text="Check Next Routine Task", command=show_next_task)
action_button.pack(pady=10)

output_label = Label(window, text="", font=("Helvetica", 10, "bold"))
output_label.pack(pady=10)

window.mainloop()