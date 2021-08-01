# Imports
import os
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.constants import LEFT, RIGHT, TOP, BOTTOM, BOTH, END, HORIZONTAL, VERTICAL, X, Y

# Colors
color_primary = '#FFFFFF'
color_secondary = '#404040'
color_dark = '#23272A'
color_accent = '#7289DA'
color_accentLight = '#697EC7'

# Initial configuration
root = tk.Tk()
root.title('Workspace')
root.geometry('1200x500')
root.resizable(False, False)
root.configure(background = color_primary)

workspace = []

if os.path.isfile('workspace.txt'):
    with open('workspace.txt', 'r') as f:
        temp = f.read()
        temp = temp.split('\n')
        workspace = [x for x in temp if x.strip()]

def add():
    file = filedialog.askopenfilename(
        initialdir='/',
        title='Select File',
        filetypes=(('EXE', '*.exe'), ('ALL', '*.*'))
    )

    if file:
        listbox.delete(0, END)
        if not file in workspace:
            workspace.append(file)
            for app in workspace:
                listbox.insert(END, app)
                listbox.itemconfig(END, selectbackground = color_dark, selectforeground = color_accent)
        elif file and file in workspace:
            messagebox.showerror(title = 'Error', message = 'This app is already on the list!')

def save():
    with open('workspace.txt', 'w') as f:
        for app in workspace:
            f.write(app + '\n')

def remove():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        workspace.pop(sum(selected))
    else:
        messagebox.showerror(title = 'Error', message = 'No item selected!')

def run():
    for app in workspace:
        os.startfile(app)

canvas = tk.Canvas(root, background = color_secondary, highlightthickness = 0)
canvas.pack(fill = BOTH, expand = True, side = TOP)

hsContainer = tk.Frame(canvas)
hsContainer.pack(side = BOTTOM, fill = X)

listbox = tk.Listbox(canvas, background = color_secondary, foreground = color_primary, borderwidth = 0, highlightthickness = 0, font = ('DaunPenh', 18), activestyle = 'none')
listbox.pack(side = LEFT, fill = BOTH, expand = True)

hs = tk.Scrollbar(hsContainer, orient = HORIZONTAL)
vs = tk.Scrollbar(canvas, orient = VERTICAL)

hs.pack(side = BOTTOM, fill = X)
vs.pack(side = RIGHT, fill = Y)

hs.config(command = listbox.xview)
vs.config(command = listbox.yview)

listbox.config(xscrollcommand = hs.set, yscrollcommand = vs.set)

frame = tk.Frame(root, background = color_dark, padx = 5, pady = 5)
frame.pack(side = BOTTOM)

buttonAdd = tk.Button(
    frame,
    text = 'ADD NEW',
    font = ('DaunPenh', 10),
    background = color_accent,
    activebackground = color_accentLight,
    foreground = color_primary,
    activeforeground = color_primary,
    border = 0,
    width = 200,
    pady = 5,
    command = add
)
buttonAdd.pack(pady = (0, 5))

buttonRun = tk.Button(
    frame,
    text = 'REMOVE SELECTED',
    font = ('DaunPenh', 10),
    background = color_accent,
    activebackground = color_accentLight,
    foreground = color_primary,
    activeforeground = color_primary,
    border = 0,
    width = 200,
    pady = 5,
    command = remove
)
buttonRun.pack(pady = (0, 5))

buttonSave = tk.Button(
    frame,
    text = 'SAVE WORKSPACE',
    font = ('DaunPenh', 10),
    background = color_accent,
    activebackground = color_accentLight,
    foreground = color_primary,
    activeforeground = color_primary,
    border = 0,
    width = 200,
    pady = 5,
    command = save
)
buttonSave.pack(pady = (0, 5))

buttonRun = tk.Button(
    frame,
    text = 'RUN WORKSPACE',
    font = ('DaunPenh', 10),
    background = color_accent,
    activebackground = color_accentLight,
    foreground = color_primary,
    activeforeground = color_primary,
    border = 0,
    width = 200,
    pady = 5,
    command = run
)
buttonRun.pack()

for app in workspace:
    listbox.insert(END, app)
    listbox.itemconfig(END, selectbackground = color_dark, selectforeground = color_accent)

# Start program
root.mainloop();
