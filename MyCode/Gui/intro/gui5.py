from tkinter import *

class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(command=self.callback, fg='red', bg='black',
                    relief=RAISED, bd=5)

    def callback(self):
        print('Goodbye world...')
        self.quit()

if __name__ == '__main__':
    HelloButton(text='Hello subclass world').mainloop()
