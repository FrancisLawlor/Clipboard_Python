#!/usr/bin/python

import getopt
import Tkinter
from Tkinter import *

# Get value inserted to entry at time of rendering.
def getValue(entry):
    return lambda: copyToClipboard(entry)
    
# Copy the contents of the entry field to the clipboard by clearing and then appending.
def copyToClipboard(entry):
    entry.clipboard_clear()
    entry.clipboard_append(entry.get())

# Insert lines from file to entry fields in the gui.
def drawGui(filename):
    f = open(filename,'r')

    window = Tkinter.Tk()
    window.title="Clipboard"

    # Row number
    r = 1

    for line in f:
        entry = Entry()
        
        # Add each line from the file without the '\n' character.
        entry.insert(END, line[:-1])
        entry.grid(row = r, column = 2)
        button = Button(text = r, command = getValue(entry))
        button.grid(row = r, column = 1)
        r = r + 1

    window.mainloop()

filename = ""

# Handle filename input.

try:
    opts, args = getopt.getopt(sys.argv[1:], 'l:')
except getopt.GetoptError:
    print("Invalid input.")
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-l'):
        filename = arg
        if(filename == ""):
            print("Filename required.")
            sys.exit(2)
    else:
        print("Invalid Input")
        sys.exit(2)

if(filename == ""):
    print("Filename required.")
    sys.exit(2)
            
drawGui(filename)
