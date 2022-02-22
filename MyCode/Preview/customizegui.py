from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):
    def reply(self):                                # наследует метод __init__
        showinfo(title='popup', message='Ouch!') # замещает метод reply

if __name__=='__main__':
    CustomGui().pack()
    mainloop()
    
    
