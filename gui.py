import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title("Complete Tkinter Demo")
root.geometry("900x800")

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

tk.Label(root, text="Tkinter Full Demo", font=("Arial", 16)).pack(pady=10)

entry_frame = tk.Frame(root)
entry_frame.pack()

tk.Label(entry_frame, text="First Name").grid(row=0, column=0)
tk.Label(entry_frame, text="Last Name").grid(row=1, column=0)

entry1 = tk.Entry(entry_frame)
entry2 = tk.Entry(entry_frame)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

check_frame = tk.Frame(root)
check_frame.pack(pady=10)

var1 = tk.IntVar()
var2 = tk.IntVar()

tk.Checkbutton(check_frame, text="Male", variable=var1).pack(side="left")
tk.Checkbutton(check_frame, text="Female", variable=var2).pack(side="left")

radio_frame = tk.Frame(root)
radio_frame.pack()

v = tk.IntVar()
tk.Radiobutton(radio_frame, text="Option A", variable=v, value=1).pack(side="left")
tk.Radiobutton(radio_frame, text="Option B", variable=v, value=2).pack(side="left")

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

mylist = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=5)
for i in range(30):
    mylist.insert(tk.END, "Item " + str(i))
mylist.pack(side=tk.LEFT)

scrollbar.config(command=mylist.yview)

def select(event):
    label_combo.config(text="Selected: " + combo_box.get())

label_combo = tk.Label(root, text="Selected Item:")
label_combo.pack()

combo_box = ttk.Combobox(root,
                         values=["Option 1", "Option 2", "Option 3"],
                         state="readonly")
combo_box.pack()
combo_box.set("Option 1")
combo_box.bind("<<ComboboxSelected>>", select)

scale_frame = tk.Frame(root)
scale_frame.pack(pady=10)

tk.Scale(scale_frame, from_=0, to=50).pack(side="left")
tk.Scale(scale_frame, from_=0, to=100,
         orient=tk.HORIZONTAL).pack(side="left")

message = tk.Message(root, text="This is a Message widget example",
                     bg="lightgreen", width=300)
message.pack(pady=10)

mb = tk.Menubutton(root, text="Options", relief=tk.RAISED)
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu

cVar = tk.IntVar()
aVar = tk.IntVar()

mb.menu.add_checkbutton(label="Contact", variable=cVar)
mb.menu.add_checkbutton(label="About", variable=aVar)
mb.pack()

tk.Spinbox(root, from_=0, to=10).pack(pady=10)

text_widget = tk.Text(root, height=3, width=40)
text_widget.pack()
text_widget.insert(tk.END, "This is a Text widget\n")

canvas = tk.Canvas(root, width=300, height=100)
canvas.pack(pady=10)
canvas.create_line(0, 50, 300, 50)

def start_progress():
    progress.start()
    for i in range(101):
        time.sleep(0.02)
        progress["value"] = i
        root.update_idletasks()
    progress.stop()

progress = ttk.Progressbar(root,
                           orient="horizontal",
                           length=300,
                           mode="determinate")
progress.pack(pady=10)

tk.Button(root, text="Start Progress",
          command=start_progress).pack()

def open_new_window():
    top = tk.Toplevel(root)
    top.title("Secondary Window")
    tk.Label(top, text="This is a Toplevel window").pack(pady=20)

tk.Button(root, text="Open New Window",
          command=open_new_window).pack(pady=10)

tk.Button(root, text="Close App",
          command=root.destroy).pack(pady=20)

root.mainloop()
