import sys
from tkinter import *

class HelloClass:
    def __init__(self):
        widget = Button(None, text = 'Hellow event world', command=self.quit)
        widget.pack()

    def quit(self):
        print('Hellow class metod world')
        sys.exit()
HelloClass()
mainloop()
