"""
кнопка Quit, которая запрашивает подтверждение на завершение;
для повторного использования достаточно прикрепить экземпляр к другому
груфическому интерфейсу и скомпоновать с желаемыми параметрами
"""

from tkinter import *
from tkinter.messagebox import askokcancel

class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Выйти', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Закрытие приложения', 'Точно выйти?')
        if ans: Frame.quit(self)

if __name__ == '__main__':
    Quitter().mainloop()
