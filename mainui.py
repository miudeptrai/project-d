import dearpygui.dearpygui as pg
import tkinter as tk
from tkinter import filedialog
import json

with open("storage.json", 'r') as sf:
    data = json.load(sf)

#GUI
pg.create_context()
pg.create_viewport(title="project-d", width=800, height=600)

def choose_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[
            ("All Files", "*.*")
        ]
    )

    root.destroy()

    if file_path:
        data["selected_file"] = file_path
        print("Selected:", data["selected_file"])
        pg.set_value("selected_file", file_path)

with pg.window(
    label="Main Window",
    tag="main_window",
    width=800,
    height=600
):
    pg.add_button(label="Browse", callback=choose_file)
    pg.add_input_text(tag="selected_file", width=400)

pg.set_primary_window("main_window", True)

pg.setup_dearpygui()
pg.show_viewport()
pg.start_dearpygui()
pg.destroy_context()