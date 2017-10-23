from Tkinter import *
import ttk
from PIL import ImageTk , Image
from main import *

Value = True

def clear_textbox():
        entry.delete(0, END)

def signal_interpreter():
    global Value
    while(Value = True):
        letter = proc_sinais()
        if (letter.isalum() = True):
            entry.insert(0,letter)



root = Tk()

root.title("MORSE - IEEE - ComSoc")
path="/home/daniel/IEEE/Morse-SENE-IEEE/Codigos/images/signal.jpg"
img = ImageTk.PhotoImage(Image.open(path))

title = Label(root,text="SIGNAL INTERPRETATION SYSTEM")
title.pack()

image_title = Label(root,text="Guideline:")
image_title.pack()
image = Label(root,image=img)
image.pack()

message = Label(root,text="Message:")
message.pack()
entry = Entry(root)
entry.pack(side=BOTTOM)
#entry = Label(root,text="None.")
#entry.pack(side=BOTTOM)
start_button = Button(root,text="Start",command=signal_interpreter)
start_button.pack(side=LEFT)
clear_button = Button(root,text="Clear",command=clear_textbox)
clear_button.pack(side=RIGHT)

#Label(root,text="Interpretation Period (Hz):").grid(row=2,column=7)
#Entry(root).grid(row=3,column=7)
#Button(root,text="Adjust").grid(row=3,column=8)
#Label(root,text="History:").grid(row=6,column=7)
#Entry(root).grid(row=7,column=7)
#Button(root,text="Clear").grid(row=7,column=8)

root.resizable(False,False)

root.mainloop()
