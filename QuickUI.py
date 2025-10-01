import tkinter as tK
from tkinter import ttk, messagebox

root = None
frame = None

# Create a window screen with padding, title and dimensions
def create_window(user_padding: int=5, title: str="QuickUI title", dimensions: tuple[int, int]=(720, 640)):
    global root, frame
    root = tK.Tk()
    frame = ttk.Frame(root, padding=user_padding)
    frame.grid()
    root.title(title)
    root.geometry(f"{dimensions[0]}x{dimensions[1]}")


# Creates a label with a set message and at a set positions
def create_label(info: str="Message", x: int=0, y: int=0):
    if frame:
        ttk.Label(frame, text=info).grid(column=x, row=y)
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a button at a set positions
def create_button(info: str="Button", x: int=0, y: int=0):
    if frame:
        ttk.Button(frame, text=info).grid(column=x, row=y)
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a entry with a set message and at positions
def create_entry(x=0, y=0, default=""):
    if frame:
        entry = ttk.Entry(frame)
        entry.insert(0, default)
        entry.grid(column=x, row=y)
        return entry
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a checkbox with info and positions
def create_checkbox(info="Check", x=0, y=0):
    if frame:
        var = tK.BooleanVar()
        ttk.Checkbutton(frame, text=info, variable=var).grid(column=x, row=y)
        return var
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a dialouge box with title and message
def show_message(title="QuickUI", message="QuickUI pop-up"):
    messagebox.showinfo(title, message)


# Refreshes UI
def refresh_ui():
    if root:
        root.mainloop()
    else:
        raise RuntimeError("Window not created. Call create_window first.")
