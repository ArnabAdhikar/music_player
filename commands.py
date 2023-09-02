from tkinter import ttk, filedialog
import os
def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        music = os.listdir(path)
        return music
