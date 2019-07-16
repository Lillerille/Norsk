# Richárd Bagi, Projekt 2019

from tkinter import *
from tkinter.filedialog import askopenfilename

def inpfil():
    """Den här funktionen tar emot en textfil och konverterar dess innehåll
    till en sträng."""
    m = Tk()
    a = askopenfilename()
    with open (a, "r") as inp:
        string=inp.read().replace('\n',' ')
    m.destroy()
    m.mainloop
    return string
