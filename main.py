import Tkinter as tk
import tkFileDialog
import pandas as pd
import xlrd
from random import randint
import sys
import tkinter.messagebox




#repeat = 0
class App(tk.Tk):

    global repeat   
    
    def __init__(self):
        tk.Tk.__init__(self) # create window

        self.filename = "" # variable to store filename
        global repeat
        repeat = tk.IntVar()
        tk.Button(self, text='Choose Name List', command=self.openfile).pack()
        tk.Button(self, text='Randomize!', command=self.randomize).pack()
        tk.Checkbutton(self, text="Repeat", variable=repeat).pack()
        self.mainloop() 


    def openfile(self):
        self.filename = tkFileDialog.askopenfilename(title="Open file")

    def randomize(self):
        alreadyChosen = []
        global repeat
        df = pd.read_excel(self.filename)
        nameList =  df.as_matrix()
        firstNames = []
        for i in range(len(nameList)):
            if i>0 and i<len(nameList):
                print nameList[i][0]
                firstNames.append(nameList[i][0])
        print 'first name list', firstNames
        number = randint(0,len(nameList)-2)
        alreadyChosen.append(number)
        print "number is: ", number
        check = True
        for j in range(len(alreadyChosen)):
            if j == number:
                check = False
                self.randomize()
                break
        print 'THE NAME:', firstNames[number]
        tk.Label(self, text=firstNames[number]).pack()
        


if __name__ == '__main__':
    App()