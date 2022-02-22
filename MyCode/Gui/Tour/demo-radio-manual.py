"""
переключатели, сложный способ (без переменных)
обратите внимание, что метод deselect переключателя просто устанавливает пустую
строку в качестве его значения, поэтому нам по прежднему требуется присвоить
переключателям уникальные значения или использовать флажки 
"""

from tkinter import *
state = ''
buttons = []

def onPress(i):
    state = i
    for bnt in buttons:
        bnt.deselect()
    buttons[i].select()

root = Tk()
for i in range(10):
    rad = Radiobutton(root, text=str(i),
                      value=str(i), command=(lambda i=i: onPress(i)))
    rad.pack(side=LEFT)
    buttons.append(rad)

onPress(0)
root.mainloop()
print(state)
    
