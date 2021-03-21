import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("Shit Todo List")

# Define add_task
def add_task():
    task = entry_tasks.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_tasks.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showinfo(title="Warning!", message="You must enter a argument")

# Define rem_task
def rem_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showinfo(title="Error", message="No task selected or no tasks in list")

# Define load_task
def load_task():
    try:
        tasks = pickle.load(open("shits.shit", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showinfo(title="Error", message="No shits.shit file found")

# Define save_task
def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("shits.shit", "wb"))

# GUI Creation
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=5, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

entry_tasks = tkinter.Entry(root, width=53)
entry_tasks.pack()

# Scrollbar
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Buttons
button_add_task = tkinter.Button(root, text="Add a item to list", width=48, command=add_task)
button_add_task.pack()

button_rem_task = tkinter.Button(root, text="Remove selected item", width=48, command=rem_task)
button_rem_task.pack()

button_load_task = tkinter.Button(root, text="Load a list", width=48, command=load_task)
button_load_task.pack()

button_save_task = tkinter.Button(root, text="Save current list", width=48, command=save_task)
button_save_task.pack()

root.mainloop()