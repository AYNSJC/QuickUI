import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser
from typing import Callable, Optional, Any

root = None
frame = None
widget_registry = []

# Create a window screen with padding, title and dimensions
def create_window(user_padding: int=5, title: str="QuickUI title", dimensions: tuple[int, int]=(720, 640)):
    global root, frame, widget_registry
    root = tk.Tk()
    frame = ttk.Frame(root, padding=user_padding)
    frame.grid()
    root.title(title)
    root.geometry(f"{dimensions[0]}x{dimensions[1]}")
    widget_registry = []


# Creates a label with a set message and at a set positions
def create_label(info: str="Message", x: int=0, y: int=0, font: Optional[tuple]=None):
    if frame:
        label = ttk.Label(frame, text=info, font=font)
        label.grid(column=x, row=y)
        widget_registry.append(label)
        return label
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a button at a set positions
def create_button(info: str="Button", x: int=0, y: int=0, command=None):
    if frame:
        button = ttk.Button(frame, text=info, command=command)
        button.grid(column=x, row=y)
        widget_registry.append(button)
        return button
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates an entry with a set message and at positions
def create_entry(x=0, y=0, default=""):
    if frame:
        entry = ttk.Entry(frame)
        entry.insert(0, default)
        entry.grid(column=x, row=y)
        widget_registry.append(entry)
        return entry
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a checkbox with info and positions
def create_checkbox(info="Check", x=0, y=0):
    if frame:
        var = tk.BooleanVar()
        checkbox = ttk.Checkbutton(frame, text=info, variable=var)
        checkbox.grid(column=x, row=y)
        widget_registry.append(checkbox)
        return var
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a dropdown/combobox with options
def create_dropdown(options: list[str], x: int=0, y: int=0, default: int=0):
    if frame:
        var = tk.StringVar(value=options[default] if options else "")
        dropdown = ttk.Combobox(frame, textvariable=var, values=options, state="readonly")
        dropdown.grid(column=x, row=y)
        widget_registry.append(dropdown)
        return var
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a spinbox for numeric input
def create_spinbox(x: int=0, y: int=0, from_: int=0, to: int=100, default: int=0):
    if frame:
        var = tk.IntVar(value=default)
        spinbox = ttk.Spinbox(frame, from_=from_, to=to, textvariable=var)
        spinbox.grid(column=x, row=y)
        widget_registry.append(spinbox)
        return var
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a text widget for multi-line input
def create_text(x: int=0, y: int=0, width: int=30, height: int=5):
    if frame:
        text = tk.Text(frame, width=width, height=height)
        text.grid(column=x, row=y)
        widget_registry.append(text)
        return text
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a listbox with selectable items
def create_listbox(items: list[str], x: int=0, y: int=0, height: int=5):
    if frame:
        listbox = tk.Listbox(frame, height=height)
        for item in items:
            listbox.insert(tk.END, item)
        listbox.grid(column=x, row=y)
        widget_registry.append(listbox)
        return listbox
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a progress bar
def create_progressbar(x: int=0, y: int=0, width: int=200, max_value: int=100):
    if frame:
        var = tk.DoubleVar()
        pbar = ttk.Progressbar(frame, variable=var, maximum=max_value, length=width)
        pbar.grid(column=x, row=y)
        widget_registry.append(pbar)
        return var
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a scale/slider widget
def create_slider(x: int=0, y: int=0, from_: int=0, to: int=100, orient: str="horizontal"):
    if frame:
        var = tk.IntVar()
        slider = ttk.Scale(frame, from_=from_, to=to, variable=var, orient=orient)
        slider.grid(column=x, row=y)
        widget_registry.append(slider)
        return var
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a separator (horizontal or vertical line)
def create_separator(x: int=0, y: int=0, orient: str="horizontal"):
    if frame:
        sep = ttk.Separator(frame, orient=orient)
        sep.grid(column=x, row=y, sticky="ew")
        widget_registry.append(sep)
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Creates a frame for grouping widgets
def create_frame(x: int=0, y: int=0, padding: int=5):
    if frame:
        sub_frame = ttk.Frame(frame, padding=padding)
        sub_frame.grid(column=x, row=y)
        widget_registry.append(sub_frame)
        return sub_frame
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")


# Dialog box functions
def show_message(title="QuickUI", message="QuickUI pop-up"):
    messagebox.showinfo(title, message)


def show_error(title="Error", message="An error occurred"):
    messagebox.showerror(title, message)


def show_warning(title="Warning", message="Warning message"):
    messagebox.showwarning(title, message)


def show_question(title="Question", message="Do you agree?"):
    return messagebox.askyesno(title, message)


def show_file_dialog(title="Open File", file_types=[("All Files", "*.*")]):
    return filedialog.askopenfilename(title=title, filetypes=file_types)


def show_save_dialog(title="Save File", file_types=[("All Files", "*.*")]):
    return filedialog.asksaveasfilename(title=title, filetypes=file_types)


def show_folder_dialog(title="Select Folder"):
    return filedialog.askdirectory(title=title)


def show_color_picker(title="Pick a Color"):
    color = colorchooser.askcolor(title=title)
    return color[1] if color[0] else None


# Remove UI widgets
def remove_widget(widget):
    """Remove a specific widget from the UI"""
    if widget in widget_registry:
        widget.grid_remove()
        widget_registry.remove(widget)


def remove_all_widgets():
    """Remove all widgets from the frame"""
    for widget in widget_registry:
        widget.grid_remove()
    widget_registry.clear()


def clear_frame():
    """Clear all widgets and reset the frame"""
    global frame
    if frame:
        for widget in widget_registry:
            widget.destroy()
        widget_registry.clear()


# Refreshes UI
def refresh_ui():
    if root:
        root.mainloop()
    else:
        raise RuntimeError("Window not created. Call create_window first.")


# Additional utility functions
def get_root():
    return root


def close_window():
    if root:
        root.quit()


def set_window_size(width: int, height: int):
    if root:
        root.geometry(f"{width}x{height}")


def set_window_title(title: str):
    if root:
        root.title(title)