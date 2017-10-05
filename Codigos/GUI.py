from Tkinter import *
import ttk
from PIL import ImageTk , Image

def GUI():
root = Tk()
    root.title("MORSE")
    path="/home/daniel/IEEE/Morse-SENE-IEEE/Codigos/images/signal.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    Label(root,text="Signal Interpretation System").grid(row=0,column=5)
    Label(root,text="Signal:").grid(row=2,column=0)
    Label(root,image=img).grid(row=3,column=0)
    Label(root,text="Message:").grid(row=6,column=0)
    Entry(root).grid(row=7,column=0)
    Button(root,text="Clear").grid(row=7,column=1)
    Label(root,text="Interpretation Period (Hz):").grid(row=2,column=7)
    Entry(root).grid(row=3,column=7)
    Button(root,text="Adjust").grid(row=3,column=8)
    Label(root,text="History:").grid(row=6,column=7)
    Entry(root).grid(row=7,column=7)
    Button(root,text="Clear").grid(row=7,column=8)
    root.resizable(False,False)
root.mainloop()

