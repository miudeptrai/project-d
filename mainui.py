import dearpygui.dearpygui as pg
import tkinter as tk
from tkinter import filedialog
import json
from arithmetic import AEngine as engine

with open("storage.json", 'r') as sf:
    data = json.load(sf)

#Callback
def submit_callback():
    data["password"] = pg.get_value("password")

def get_password_callback():
    pg.set_value("password_displayer", data["password"])

#GUI
pg.create_context()
pg.create_viewport(title="project-d", width=800, height=600)

with pg.window(
    label="Main Window",
    tag="main_window",
    width=800,
    height=600
):
    with pg.group(horizontal=True):
        pg.add_text("Password:")
        pg.add_input_text(tag="password")
        pg.add_button(label="Submit", callback=submit_callback)
    
    with pg.group(horizontal=True):
        pg.add_button(label="Get password", callback=get_password_callback)
        pg.add_input_text(default_value="", readonly=True, tag="password_displayer")

pg.set_primary_window("main_window", True)

print("Here")
pg.setup_dearpygui()
pg.show_viewport()
pg.start_dearpygui()
pg.destroy_context()