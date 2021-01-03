import sys, os, pathlib
import zipfile

from tkinter import filedialog
import tkinter as tk

class Zipper:

    def __init__(self):
        if getattr(sys, 'frozen', False):
            script_path = os.path.dirname(sys.executable)
        else:
            script_path = os.path.dirname(os.path.abspath(__file__))
        self.script_path = script_path

    def ui(self, root):

        # Frame 1
        frame = tk.Frame(
            master=root
        )
        frame.grid(row=0, column=0)
        label = tk.Label(master=frame, text='Pick the folder where the files are located: ')
        label.pack()

        # Frame 2
        frame2 = tk.Frame(
            master=root
        )
        frame2.grid(row=0, column=1)
        folderPickBtn = tk.Button(master=frame2, text="Choose Folder", width=20, height=2, bg="blue")
        folderPickBtn.pack()
        folderPickBtn.bind('<Button-1>', self.getFolderPath())

    def zipIt(self, files):
        with zipfile.ZipFile('File.zip', 'w', zipfile.ZIP_DEFLATED) as zip:
            zip.write(r'C:\Users\Selim\Desktop\TEST\1.wav', '1.wav')

    def getFolderPath(self):
        pass
# creating the root of app
root = tk.Tk()
root.configure(background='white')

zp = Zipper()
zp.ui(root)


root.geometry('900x900')
root.mainloop()