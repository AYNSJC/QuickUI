from tkinter import Tk, ttk

root = None
frame = None

def create_window(user_padding: int, title: str, dimensions: tuple[int, int]):
    global root, frame
    root = Tk()
    frame = ttk.Frame(root, padding=user_padding)
    frame.grid()
    root.title(title)
    root.geometry(f"{dimensions[0]}x{dimensions[1]}")

def create_label(info: str, x: int, y: int):
    if frame:
        ttk.Label(frame, text=info).grid(column=x, row=y)
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")

def create_button(info: str, x: int, y: int):
    if frame:
        ttk.Button(frame, text=info).grid(column=x, row=y)
    else:
        raise RuntimeError("Frame not initialized. Call create_window first.")

def refresh_ui():
    if root:
        root.mainloop()
    else:
        raise RuntimeError("Window not created. Call create_window first.")
