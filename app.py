from tkinter import *
from tkinter import ttk
from task import Tasks
import calendar


to_do_list=[]
yy = 2024

def pick_day(chosen_month, chosen_day):
    day_number = calendar.weekday(yy, chosen_month, chosen_day)
    day_names = list(calendar.day_name)
    print(day_names[day_number])

def add_task():
    user_task = entry.get()
    user_task_urgency = urgency.get()
    Tasks.name = user_task
    Tasks.urgency = user_task_urgency
    to_do_list.append({"Task": Tasks.name, "Urgency": Tasks.urgency})
    display_tasks()

def display_tasks():
    text.delete('1.0', END)  
    for index, task in enumerate(to_do_list):
        task_text = f"Task: {task['Task']} - Urgency: {task['Urgency']}\n"
        tag_name = f"task_{index}" 
        text.insert(END, task_text, tag_name)
        text.tag_bind(tag_name, "<Button-1>", lambda e, tag=tag_name: toggle_finished(tag))

def toggle_finished(tag):
    current_style = text.tag_cget(tag, "overstrike")
    if current_style == "1":  
        text.tag_config(tag, overstrike=0)
    else:  
        text.tag_config(tag, overstrike=1)


def sort_tasks():
    text.delete('1.0', END)
    sorted_list = sorted(to_do_list, key=lambda task: int(task["Urgency"]))
    for index, task in enumerate(sorted_list):
        task_text = f"Task: {task['Task']} - Urgency: {task['Urgency']}\n"
        tag_name = f"task_{index}" 
        text.insert(END, task_text, tag_name)
        text.tag_bind(tag_name, "<Button-1>", lambda e, tag=tag_name: toggle_finished(tag))

def show_calendar():
    calendar_year = calendar.calendar(yy)
    text.insert(END, calendar_year)

def hide_calendar():
     text.delete('1.0', END)

window = Tk()
window.title("User Input")


label = ttk.Label(window, text="Enter Task:")
label.pack()

entry = ttk.Entry(window)
entry.pack()

urgency = StringVar()
urgency = ttk.Combobox(window, textvariable=urgency)
urgency['values'] = ('1','2','3','4','5')
urgency.state(["readonly"])
label = ttk.Label(window, text="Choose Task Urgency:")
urgency.pack()

add_task_button = ttk.Button(window, text="Submit", command=add_task)
add_task_button.pack()

text = Text(window, width=100, height=20)
text.pack()

sort_tasks_button = ttk.Button(window, text="Sort Tasks", command=sort_tasks)
sort_tasks_button.pack()

show_calendar_button = ttk.Button(window, text="Show Calendar", command=show_calendar)
show_calendar_button.pack()

hide_calendar_button = ttk.Button(window, text="Hide Calendar", command=hide_calendar)
hide_calendar_button.pack()


window.mainloop() 


# print(calendar.calendar(yy))
day_number = calendar.weekday(yy, 12, 18)
day_names = list(calendar.day_name)
print(day_names[day_number])
print(calendar.Calendar.itermonthdays(calendar, 2025, 2)) 