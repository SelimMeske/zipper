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

        for w in range(8):
            root.columnconfigure(w, weight=1)
            root.rowconfigure(w, weight=1)

        # Image Frame
        welcomeLabelFrame = tk.Frame(
            master=root
        )
        welcomeLabelFrame.grid(row=0, column=1)
        wellcomeLabel = tk.Label(master=welcomeLabelFrame, text="Welcome to Zipper.")
        wellcomeLabel.configure(background="white", font=('Arial', 25))
        wellcomeLabel.pack()

        # Frame 1
        frame = tk.Frame(
            master=root,
            pady=20,
            background="white"
        )
        frame.grid(row=1, column=0, padx=20, sticky="w")
        label = tk.Label(master=frame, text='Pick the folder where the files are located: ', font=font, anchor='nw')
        label.configure(background="white")
        label.pack()

        # Frame 2
        frame2 = tk.Frame(
            master=root
        )
        frame2.grid(row=1, column=1, sticky="w")
        folderPickBtn = tk.Button(master=frame2, relief=tk.FLAT, text="Choose Folder", width=16, height=1, bg="#FF9900", font=font,
                                  command=lambda: self.getFolderPath(label=pathLocation))
        folderPickBtn.pack()

        # Frame 3
        frame3 = tk.Frame(
            master=root
        )
        frame3.grid(row=1, column=2, sticky="w")
        pathLocation = tk.Label(master=frame3, text=self.defFolderText, font=font, padx=20)
        pathLocation.configure(background="white")
        pathLocation.pack()

        # Frame 4
        frame4 = tk.Frame(
            master=root,
            pady=20,
            background="white"
        )
        frame4.grid(row=2, column=0, padx=20, sticky="w")
        outputLocationLabel = tk.Label(master=frame4, text="Select the output folder: ", font=font)
        outputLocationLabel.configure(background="white")
        outputLocationLabel.pack(fill=tk.X)

        # Frame 5
        frame5 = tk.Frame(
            master=root
        )
        frame5.grid(row=2, column=1, sticky="w")
        outputFolderPick = tk.Button(master=frame5, relief=tk.FLAT, text="Choose Folder", width=16, height=1, bg="#FF9900", font=font,
                                     command=lambda: self.getDestinationPath(label=outputPathLocation))
        outputFolderPick.pack()

        # Frame 6
        frame6 = tk.Frame(
            master=root
        )
        frame6.grid(row=2, column=2, sticky="w")
        outputPathLocation = tk.Label(master=frame6, text=self.defFolderText, font=font, padx=20)
        outputPathLocation.configure(background="white")
        outputPathLocation.pack()

        # Frame 7
        frame7 = tk.Frame(
            master=root,
            pady=20,
            background="white"
        )
        frame7.grid(row=3, column=0, sticky="w")
        maxSizeLabel = tk.Label(master=frame7, text="Maximum size of one zip file? (MB)", font=font, padx=20)
        maxSizeLabel.configure(background="white")
        maxSizeLabel.pack()

        # Frame 8
        frame8 = tk.Frame(
            master=root
        )
        frame8.grid(row=3, column=1, sticky="w")
        maxSizeInput = tk.Text(master=frame8, border=1, width=5, height=1)
        maxSizeInput.pack()

        # Frame 9
        frame9 = tk.Frame(
            master=root
        )
        frame9.grid(row=4, column=1, sticky="w")
        startButton = tk.Button(master=frame9, relief=tk.FLAT, text="Zip it!", width=16, height=1, bg="#FF9900", font=font,
                                command=lambda: self.zipIt(destination=self.outputDestionation, folder=self.filesFolder,
                                                           entry=maxSizeInput))
        startButton.pack()

    def zipIt(self, destination, folder, entry):
        print('In Outer loop')
        if destination and folder and entry:

            print('In Our Loop')

            currentPackageSize = 0
            zipName = 'Zip'
            zipCount = 1
            maxPackageSize = int(entry.get("1.0", tk.END))

            for root, folders, files in os.walk(folder):
                for singleFile in files:
                    fileFullPath = os.path.join(folder, singleFile)
                    currentFileSize = round(os.stat(fileFullPath).st_size / 1048576, 2)
                    if currentFileSize > maxPackageSize:
                        pass
                    else:
                        if currentFileSize + currentPackageSize > maxPackageSize:
                            print('Larger')
                            zipCount += 1
                            currentPackageSize = 0

                        with zipfile.ZipFile(os.path.join(destination, zipName + str(zipCount)) + '.zip', 'a', zipfile.ZIP_DEFLATED) as zip:
                            zip.write(fileFullPath, singleFile)

                        currentPackageSize += currentFileSize
        else:
            pass

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
