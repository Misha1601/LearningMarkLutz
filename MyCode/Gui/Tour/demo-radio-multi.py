#  посмотрите что произойдет, если несколько переключателей
#  будут иметь одно и тоже значение

from tkinter import *
root = Tk()
var = StringVar()
for i in range(10):
    rad = Radiobutton(root, text=str(i), variable=var, value=str(i%2))
    rad.pack(side=LEFT)
var.set(' ')
root.mainloop()
