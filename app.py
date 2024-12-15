from tkinter import *
from tkinter import ttk
from task import Tasks

to_do_list=[]

def print_to_do_list():
    print(to_do_list)

def add_task():
    user_task = entry.get()
    user_task_urgency = urgency.get()
    Tasks.name = user_task
    Tasks.urgency = user_task_urgency
    to_do_list.append({"Task": Tasks.name, "Urgency": Tasks.urgency})
    print_to_do_list()

def display_tasks():
    text.delete('1.0', END)  # Clear previous content
    for task in to_do_list:
        text.insert(END, f"{task}\n")  # Insert each task into the Text widget
    

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
display_tasks_button = ttk.Button(window, text="Show My Tasks", command=display_tasks)
display_tasks_button.pack()

window.mainloop() 


