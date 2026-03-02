import tkinter
import tkinter as tk
from tkinter import ttk
import time
from tkinter import PhotoImage
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Complete Tkinter Demo")
# root.geometry("900x800")


# menu = tk.Menu(root)
# root.config(menu=menu)
#
# filemenu = tk.Menu(menu, tearoff=0)
# menu.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="New")
# filemenu.add_command(label="Open")
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.quit)
#
# helpmenu = tk.Menu(menu, tearoff=0)
# menu.add_cascade(label="Help", menu=helpmenu)
# helpmenu.add_command(label="About")

# tk.Label(root, text="Tkinter Full Demo", font=("Arial", 16)).pack(pady=10)

message = tk.Message(root, text="Welcome Name!",
                     bg="lightgreen", width=300)
message.pack(pady=10)

entry_frame = tk.Frame(root)


def perform_search():
    search_term = search_entry.get()
    if search_term:
        result_label.config(text=f"Searching for: {search_term}")
        if search_term.lower() == 'python':
            print("Found 'python'!")
    else:
        result_label.config(text="Please enter a search term.")

# root = tk.Tk()
# root.title("Tkinter Search Example")

search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=perform_search)
search_button.pack(pady=5)

result_label = tk.Label(root, text="Enter a movie and click Search!")
result_label.pack(pady=10)


entry1 = tk.Entry(entry_frame)
entry1.grid(row=0, column=1)
#
# message = tk.Message(root, text="Today's Top Picks For You!",
#                      bg="lightgreen", width=300)
# message.pack(pady=10)
# #
canvas = tk.Canvas(root, width=300, height=100)
canvas.pack(pady=10)
canvas.create_line(0, 50, 300, 50)


tk.Button(root, text="Close App",
          command=root.destroy).pack(pady=20)

root.mainloop()
