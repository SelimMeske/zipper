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
        self.outputDestionation = None
        self.filesFolder = None

    def ui(self, root):

        # Frame 1
        frame = tk.Frame(
            master=root,
            pady=20,
            background="white"
        )
        frame.grid(row=0, column=0, padx=20)
        label = tk.Label(master=frame, text='Pick the folder where the files are located: ', font=font, anchor='nw')
        label.configure(background="white")
        label.pack()

        # Frame 2
        frame2 = tk.Frame(
            master=root
        )
        frame2.grid(row=0, column=1)
        folderPickBtn = tk.Button(master=frame2, text="Choose Folder", width=16, height=1, bg="#FF9900", font=font, command=lambda: self.getFolderPath(label=pathLocation))
        folderPickBtn.pack()

        # Frame 3
        frame3 = tk.Frame(
            master=root
        )
        frame3.grid(row=0, column=2)
        pathLocation = tk.Label(master=frame3, text=self.defFolderText, font=font, padx=20)
        pathLocation.configure(background="white")
        pathLocation.pack()

        # Frame 4
        frame4 = tk.Frame(
            master=root,
            pady=20,
            background="white"
        )
        frame4.grid(row=1, column=0, padx=20)
        outputLocationLabel = tk.Label(master=frame4, text="Select the output folder: ", font=font)
        outputLocationLabel.configure(background="white")
        outputLocationLabel.pack()

        # Frame 5
        frame5 = tk.Frame(
            master=root
        )
        frame5.grid(row=1, column=1, sticky="ew")
        outputFolderPick = tk.Button(master=frame5, text="Choose Folder", width=16, height=1, bg="#FF9900", font=font, command=lambda: self.getDestinationPath(label=outputPathLocation))
        outputFolderPick.pack()

        # Frame 6
        frame6 = tk.Frame(
            master=root
        )
        frame6.grid(row=1, column=2)
        outputPathLocation = tk.Label(master=frame6, text=self.defFolderText, font=font, padx=20)
        outputPathLocation.configure(background="white")
        outputPathLocation.pack()

        # Frame 7
        frame7 = tk.Frame(
            master=root,
            pady=20,
            background="white"
        )
        frame7.grid(row=2, column=0)
        maxSizeLabel = tk.Label(master=frame7, text="Maximum size of one zip file? (MB)", font=font, padx=20)
        maxSizeLabel.configure(background="white")
        maxSizeLabel.pack()

        # Frame 8
        frame8 = tk.Frame(
            master=root
        )
        frame8.grid(row=2, column=1)
        maxSizeInput = tk.Entry(master=frame8, border=2, width=5)
        maxSizeInput.pack()

        # Frame 9
        frame9 = tk.Frame(
            master=root
        )


    def zipIt(self, destination, folder):
        with zipfile.ZipFile('File.zip', 'w', zipfile.ZIP_DEFLATED) as zip:
            zip.write(r'C:\Users\Selim\Desktop\TEST\1.wav', '1.wav')

    def getFolderPath(self, label):
        path = filedialog.askdirectory()
        if path:
            label.configure(text=path)
            self.filesFolder = path
        else:
            label.configure(text=self.defFolderText)

    def getDestinationPath(self, label):
        path = filedialog.askdirectory()
        if path:
            label.configure(text=path)
            self.outputDestionation = path
        else:
            label.configure(text=self.defFolderText)


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