"""
4 класса демонстрационных компонентов (вложенных фрэймов) в одном окне;
в одном окне присутствуют так же 5 окон Quitter, причем щелчок на любой из
нихприводит к завершению программы; графические интерфейсы могут повторно
использоваться, как фрэймы в контейнере. независимые окна или процессы;
"""

from tkinter import *
from quitter import Quitter
demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']
parts = []

def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)
        part = module.Demo(root)
        part.config(bd=2, relief=GROOVE)
        part.pack(side=LEFT, expand=YES, fill=BOTH)
        parts.append(part)

def dumpState():
    for part in parts:
        print(part.__module__+ ':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')

root = Tk()
root.title('Frames')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()
