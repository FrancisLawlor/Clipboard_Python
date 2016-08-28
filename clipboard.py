#!/usr/bin/python

import Tkinter
from Tkinter import *

def getValue(entry):
    return lambda: copyToClipboard(entry)
    
def copyToClipboard(entry):
    entry.clipboard_clear()
    entry.clipboard_append(entry.get())
    
f = open('words.txt','r')

window = Tkinter.Tk()
window.title="Clipboard"

# Row number
r = 1

for line in f:
    entry = Entry()
    entry.insert(END, line)
    entry.grid(row=r, column=2)
    button = Button(text=r, command=getValue(entry))
    button.grid(row=r, column=1)
    r = r + 1

window.mainloop()
