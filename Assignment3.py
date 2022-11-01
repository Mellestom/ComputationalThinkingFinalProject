"""
Created on Spring 2022

Assignment 3 ~ Part A

@author: Group Member Name

"""

import tkinter
from tkinter import *
from PIL import Image, ImageTk
import csv 
#import partB as b
#import partC as c
import pandas as pd

class AllTkinterWidgets:
    def __init__(self, master):
        frame = Frame(master,width=800, height=800)
        frame.place(x=0, y=0)

       # -------------------- Label frame ------------------------
        self.lb1 = Label(frame, text= '2021 Chicago Traffic Crashes Data Analysis',font=(12))
        self.lb1.pack(fill = X, side = TOP)

       # ------------------- PartB menu ---------------------
        self.mbar = Frame(frame, relief = 'raised',  bd = 2)
        self.mbar.pack(expand = 0, fill = X, side = TOP)

        self.fgbutton = Menubutton(self.mbar, text = 'PartB')
        self.fgbutton.pack(side = LEFT)
        self.fgmenu = Menu(self.fgbutton, tearoff=0)
        self.fgbutton['menu'] = self.fgmenu

        # Populate part B menu
        #self.fgmenu.add('command', label = 'Injury', command = self.Injury)
        #self.fgmenu.add('command', label = 'NotifiedDelay', command = self.NotifiedDelay)
        #self.fgmenu.add('command', label = 'StreetCrash', command = self.StreetCrash)
       
       # ------------------- Entry box frame and entry---------------

        self.fentry = Entry(frame,bd = 3)
        self.load = Button(frame, text = "Load", command = self.UploadFile)
        self.load.pack()
        self.fentry.pack()

       # ------------------- PartC frame and buttons-----------------




       # --------------------- Listbox frame -----------------------
        self.lf = Frame(frame,height=260)
        self.lf.pack_propagate(False)
        #self.bt5 = Button(self.lf, text = 'Clear', command = self.clear)
        self.listbox = Listbox(self.lf)
        self.sbl = Scrollbar(self.listbox, orient=VERTICAL, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=self.sbl.set)
        self.sbl.pack(side=RIGHT, fill=Y)
        self.listbox.pack(expand=1,side=TOP, padx=5, fill = BOTH)
        #self.bt5.pack(before=self.listbox,side=BOTTOM)
        self.lf.pack(fill=BOTH, pady=5)



       # -------------------- Function definitions ------------------------

    def UploadFile(self):
        file = open('Traffic_Crashes_2021.csv', 'r')
        try:    
            reader = csv.reader(file)
            FindInjury = 'Injury'
            FindNoInjury = 'No Injury'
            CountInjury = 0
            Noinjury = 0
            for line in reader:
        
                if FindNoInjury in line:
                    Noinjury+=1
                else:
                    CountInjury+=1
                
                      
        finally:
            print(CountInjury)
            print(Noinjury)
            file.close()
            


# main--setup tkinter object, instantiate AllTkinterWidgets class and display
root = Tk()
root.geometry('1000x800')
root.configure(bg='black')
root.resizable(width=True, height=True)
all = AllTkinterWidgets(root)
root.title('Computational Thinking ~ Assignment 3')
root.mainloop()






