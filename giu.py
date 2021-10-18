import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

def CreateWidgets():
    link_Label = Label(root, text ="Select The File For Transfer : ",#title of lable
                    bg = "#E8D579")#background color
    link_Label.grid(row = 1, column = 0,
                    pady = 5, padx = 5)
     
    root.sourceText = Entry(root, width = 50,
                            textvariable = sourceLocation)
    root.sourceText.grid(row = 1, column = 1,
                        pady = 5, padx = 5,
                        columnspan = 2)
     
    source_browseButton = Button(root, text ="Browse",
                                command = SourceBrowse, width = 15)
    source_browseButton.grid(row = 1, column = 3,
                            pady = 5, padx = 5)
     
    destinationLabel = Label(root, text ="Select The Destination : ",
                            bg ="#E8D579")
    destinationLabel.grid(row = 2, column = 0,
                        pady = 5, padx = 5)
     
    root.destinationText = Entry(root, width = 50,
                                textvariable = destinationLocation)
    root.destinationText.grid(row = 2, column = 1,
                            pady = 5, padx = 5,
                            columnspan = 2)
     
    dest_browseButton = Button(root, text ="Browse",
                            command = DestinationBrowse, width = 15)
    dest_browseButton.grid(row = 2, column = 3,
                        pady = 5, padx = 5)
     
  
     
    moveButton = Button(root, text ="Move File",
                        command = MoveFile, width = 15)
    moveButton.grid(row = 3, column = 2,
                    pady = 5, padx = 5)
    

def SourceBrowse():
    sourcedirectory = filedialog.askdirectory(initialdir = "C:/Users/jmcke/OneDrive/Desktop/Folder C/")
    root.sourceText.insert('1', sourcedirectory)

def DestinationBrowse():
    destinationdirectory = filedialog.askdirectory(initialdir ="C:/Users/jmcke/OneDrive/Desktop/Folder D/")
    root.destinationText.insert('1', destinationdirectory)

def MoveFile():
     #files = os.listdir(source)
     destination_location = destinationLocation.get()

     for f in files:
         shutil.move(files, destination_location)
         messagebox.showinfo("Success")


root = tk.Tk()
root.title('File Transfer')
root.geometry("400x400")


sourceLocation = StringVar()
destinationLocation = StringVar()
CreateWidgets()

root.mainloop()
