from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup', message='Batton pressed!')

window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()
