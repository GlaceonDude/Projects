#Anthony Barrante
#ITP 100
#Chapter 9 Project
#This program creates a GUI Menu with options
#to Create New, Save, Open, and edit a Text File.

import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class TextEdit:

    #Initialize tkinter interpreter
    root = Tk()

    #Set default window variables
    theTextArea = Text(root)
    theMenuBar = Menu(root)
    theFileMenu = Menu(theMenuBar, tearoff=0)
    theEditMenu = Menu(theMenuBar, tearoff=0)

    #Adding Scrollbar
    theScrollbar = Scrollbar(theTextArea)
    file = None

    def __init__(self):

        #Intialize Window
        self.root.geometry("300x300")

        screeWidth= self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)

        #Intialize Title
        self.root.title("Untitled Document")

        #Setting Controls for Text Area
        self.theTextArea.grid(sticky = N + E + S + W)

        #Opens a new File
        self.theFileMenu.add_command(label="New", command=self.newFile)

        #Opens an existing file
        self.theFileMenu.add_command(label="Open", command=self.openFile)

        #Saves the Current File
        self.theFileMenu.add_command(label="Save", command=self.saveFile)

        #Quits the Text Editor // Sets Option 1 Away
        self.theFileMenu.add_separator()
        self.theFileMenu.add_command(label="Quit", command=self.quitApplication)
        #This feature makes the menu a drop-down
        self.theMenuBar.add_cascade(label="File", menu=self.theFileMenu)

        #Creates the Edit menu on the Menubar
        self.theMenuBar.add_cascade(label="Edit", menu=self.theEditMenu)

        #Allows user to use the Cut feature
        self.theEditMenu.add_command(label="Cut", command=self.cut)

        #Allows user to use the Copy feature
        self.theEditMenu.add_command(label="Copy", command=self.copy)

        #Allows the user to use the Paste Feature
        self.theEditMenu.add_command(label="Paste", command=self.paste)

        #Self Adjusting Scrollbar
        self.theScrollbar.config(command=self.theTextArea.yview)
        self.theTextArea.config(yscrollcommand=self.theScrollbar.set)

        #Show the menu
        self.root.config(menu=self.theMenuBar)
       

    def newFile(self):
        #This function allows a new file to be created
        #It also clears out the Text Widget

        #Set Title to Untitled Document
        self.root.title("Untitled Document")
        self.file = None
        self.theTextArea.delete(1.0,END)

    def openFile(self):
        #uses File Dialog import to find file to open
        #uses Dictionary to differ between all files and text files
        self.file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        #If file cannot be found
        if self.file == "":
            #no file
            self.file = None
        else:
            #Try to open the file selected
            #Sets new Title
            self.root.title(os.path.basename(self.file) + " - Document")

            #Clear the Text Widget
            self.theTextArea.delete(1.0, END)

            #Open the file
            file = open(self.file, "r")

            #Insert the contents
            self.theTextArea.insert(1.0, file.read())

            #Close the File
            file.close()

    def saveFile(self):
        #Uses File Dialog from import to save as a new document
        if self.file == None:
            #Saves the new file
            self.file = asksaveasfilename(initialfile='Untitled.txt',
                                          defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if self.file == "":
                self.file = None
            else:
                #Trys to save (write) the file
                file = open(self.file,"w")
                file.write(self.theTextArea.get(1.0, END))
                file.close()

                #Set the windows title
                self.master.title(os.path.basename(self.title) + " - Document")

        else:
            #save the file
            file = open(self.file,"w")
            file.write(self.theTextArea.get(1.0,END))
            file.close()

    def cut(self):
        #Uses File Dialog Import to Create Cut Feature
        self.theTextArea.event_generate("<<Cut>>")

    def copy(self):
        #Uses the File Dialog to Create Copy Feature
        self.theTextArea.event_generate("<<Copy>>")

    def paste(self):
        #Uses the File Dialog to Create Paste Feature
        self.theTextArea.event_generate("<<Paste>>")

    def quitApplication(self):
        #Exits the Application
        self.root.destroy()

    def run(self):
        #Runs the main application
        self.root.mainloop()


#Run Main Application
textdoc = TextEdit()
textdoc.run()
            
    
        

        
    

