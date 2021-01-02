import sys, os, zipfile, pathlib

import tkinter as tk

class Zipper:
    def __init__(self):
        if getattr(sys, 'frozen', False):
            script_path = os.path.dirname(sys.executable)
        else:
            script_path = os.path.dirname(os.path.abspath(__file__))
        self.script_path = script_path
    def ui(self):
        pass
    def createLabel(self, txt, root):
        label = tk.Label(root, text=txt)
        label.pack(padx=20, pady=20)


# creating the root of app
root = tk.Tk()

zp = Zipper()
zp.createLabel(zp.script_path, root)

root.geometry('600x600')
root.mainloop()

