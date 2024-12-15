from tkinter import *
from tkinter import ttk
from task import Tasks

to_do_list=[]

def add_task():
    user_task = entry.get()
    user_task_urgency = urgency.get()
    Tasks.name = user_task
    Tasks.urgency = user_task_urgency
    to_do_list.append({"Task": Tasks.name, "Urgency": Tasks.urgency})
    display_tasks()

def display_tasks():
    text.delete('1.0', END)  # Clear previous tasks in the Text widget
    for index, task in enumerate(to_do_list):
        task_text = f"Task: {task['Task']} - Urgency: {task['Urgency']}\n"
        tag_name = f"task_{index}" 
        text.insert(END, task_text, tag_name)
        # Bind left click to toggle the finished state
        text.tag_bind(tag_name, "<Button-1>", lambda e, tag=tag_name: toggle_finished(tag))

def toggle_finished(tag):
    # Toggle strikethrough for the task with the given tag
    current_style = text.tag_cget(tag, "overstrike")
    if current_style == "1":  # If already crossed off, remove strikethrough
        text.tag_config(tag, overstrike=0)
    else:  # If not crossed off, apply strikethrough
        text.tag_config(tag, overstrike=1)


def sort_tasks():
    text.delete(1.0, END)
    sorted_list = sorted(to_do_list, key=lambda task: int(task["Urgency"]))
    for task in sorted_list:
        print(f"Task: {task['Task']} - Urgency: {task['Urgency']}")

# Create main window
window = Tk()
window.title("User Input")

# Create label for task
label = ttk.Label(window, text="Enter Task:")
label.pack()

# Create entry field
entry = ttk.Entry(window)
entry.pack()

# Create label for prompt
urgency = StringVar()
urgency = ttk.Combobox(window, textvariable=urgency)
urgency['values'] = ('1','2','3','4','5')
urgency.state(["readonly"])
label = ttk.Label(window, text="Choose Task Urgency:")
urgency.pack()

# Create button to submit input
add_task_button = ttk.Button(window, text="Submit", command=add_task)
add_task_button.pack()

text = Text(window, width=40, height=10)
text.pack()

sort_tasks_button = ttk.Button(window, text="Sort Tasks", command=sort_tasks)
sort_tasks_button.pack()

window.mainloop() 


