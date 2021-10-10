import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Grid
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory
import pytubeCode
import linkValidator


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.localfolder = None
        self.upbar()
        self.logoimage()
        self.inputsZone()
        self.buttons()

    def upbar(self):
        self.menubar = tk.Menu(root, bg="white", fg="black")
        self.master.config(menu=self.menubar)

        self.menubar.add_command(
            label="Exit", font=("Sans"), command=self.quit)

    def logoimage(self):
        self.img = Image.open("./yticon.png")
        self.img = self.img.resize((300, 300), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.img)
        self.showImage = tk.Label(
            root, text="LogoYTDownloader", image=self.image, bg="#333")
        self.showImage.grid(row=1, column=1)

    def inputsZone(self):
        self.link = tk.Label(root, text="Insert Link: ",
                             font=("Sans"), bg="#333", fg="white")
        self.link.grid(row=2, column=0)

        self.linkVar = tk.StringVar()
        self.linkInput = tk.Entry(root, font=(
            "Sans"), width=70, textvariable=self.linkVar)
        self.linkInput.grid(row=2, column=1)

    def buttons(self):
        self.selectdownloadType = tk.Button(
            root, text="Mp3", bg="#EB2D30", fg="white", activebackground="#EB2D30", relief="groove")
        self.selectdownloadType.grid(row=2, column=2, padx=15)

        self.folder = tk.Button(root, text="Select Folder: ", font=(
            "Sans"), bg="#EB2D30", fg="white", activebackground="#EB2D30", relief="groove", command=self.findFolder)
        self.folder.grid(row=3, column=0, pady=15, padx=5)
        self.displayLocalFolder = tk.Label(
            root, text=f"{self.folder}", font=("Sans"), bg="#333", fg="white")

        self.download = tk.Button(root, text="Download", font=(
            "Sans"), bg="#FD3D40", fg="white", activebackground="#FD3D40", relief="groove", command=self.startDownload)
        self.download.grid(row=4, column=1, pady=15, ipadx=25, ipady=5)

    def findFolder(self):
        self.displayLocalFolder['text'] = ""
        self.localfolder = askdirectory()

        self.displayLocalFolder = tk.Label(
            root, text=f"{self.localfolder}", font=("Sans"), bg="#333", fg="white")
        self.displayLocalFolder.grid(row=3, column=1)

    def startDownload(self):
        self.linkGet = self.linkVar.get()
        print("Downloada ON")
        print(f"Local: {self.localfolder}")
        print(f"Link: {self.linkGet}")

        if linkValidator.validLinkfunc(self.linkGet) == True and self.localfolder != None:
            print("oi")
            if pytubeCode.CodePyTube(self, self.linkGet, self.localfolder) == False:
                self.alertDownload = messagebox.showinfo(title="ERRO", message=(
                    "ERRO: INVALID LINK\nmake sure the link passed is correct."))

            else:
                pytubeCode.CodePyTube(self, self.linkGet, self.localfolder)
                self.alertDownload = messagebox.showinfo(
                    title="download completed", message=("Donwload completed"))

        else:
            self.alertDownload = messagebox.showinfo(title="ERRO", message=(
                "ERRO: INVALID LINK\nmake sure the link passed is correct."))
            if (self.localfolder == None):
                self.alertDownload = messagebox.showinfo(
                    title="ERRO", message=("ERRO: Inform the folder"))


root = tk.Tk()
root.title("Youtube Downloader")
root.resizable(False, False)
root.configure(bg="#333")
Application(master=root)
root.mainloop()
