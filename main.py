import sys, os, pathlib
import zipfile

from tkinter import filedialog
import tkinter as tk
from tkinter.font import Font

class Zipper:

    def __init__(self):
        if getattr(sys, 'frozen', False):
            script_path = os.path.dirname(sys.executable)
        else:
            script_path = os.path.dirname(os.path.abspath(__file__))
        self.script_path = script_path
        self.defFolderText = "Please select a valid folder."

    def ui(self, root):

        # Frame 1
        frame = tk.Frame(
            master=root
        )
        frame.grid(row=0, column=0, sticky="ew", padx=20)
        label = tk.Label(master=frame, text='Pick the folder where the files are located: ', font=font)
        label.configure(background="white")
        label.pack()

        # Frame 2
        frame2 = tk.Frame(
            master=root
        )
        frame2.grid(row=0, column=1, sticky="ew")
        folderPickBtn = tk.Button(master=frame2, text="Choose Folder", width=20, height=2, bg="#FF9900", font=font, command=lambda: self.getFolderPath(pathLocation=pathLocation))
        folderPickBtn.pack()

        # Frame 3
        frame3 = tk.Frame(
            master=root
        )
        frame3.grid(row=0, column=3, sticky="ew")
        pathLocation = tk.Label(master=frame3, text=self.defFolderText, font=font, padx=20)
        pathLocation.configure(background="white")
        pathLocation.pack()

    def zipIt(self, files):
        with zipfile.ZipFile('File.zip', 'w', zipfile.ZIP_DEFLATED) as zip:
            zip.write(r'C:\Users\Selim\Desktop\TEST\1.wav', '1.wav')

    def getFolderPath(self, pathLocation):
        path = filedialog.askdirectory()
        if path:
            pathLocation.configure(text=path)
        else:
            pathLocation.configure(text=self.defFolderText)

# creating the root of app
root = tk.Tk()
root.configure(background='white')
text = tk.Text(root)

# Create a def. font
font = Font(family='Helvetica', size=12)
text.configure(font=font)

zp = Zipper()
zp.ui(root)


root.geometry('900x900')
root.mainloop()