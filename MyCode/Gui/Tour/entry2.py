"""
непосредственное использование виджетов Entry и размещение их по рядам с метками
фиксированной ширины: такой способ компановки, а так же использование менеджера
grid обеспечивают наилучшее представление для форм
"""
from tkinter import *
from quitter import Quitter

fields = 'Name', 'Job', 'Pay'

def fetch(entryes):
    for entry in entryes:
        print('Input => "%s"' % entry.get())

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=5, text=field)
        ent = Entry(row)
        row.pack(side=TOP, fill=X)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append(ent)
    return entries
if __name__ == '__main__':
    root = Tk()
    makeform(root, fields)
    #root.bind('<Return>', (lambda event: fetch(ents)))
    #Button(root, text='fetch',
    #       command=(lambda: fetch(ents))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.mainloop()
