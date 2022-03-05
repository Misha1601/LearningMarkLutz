from tkinter import *

def greeting():
    print('Hello sydout world!...')

win = Frame()
win.pack(side=TOP, expand=YES, fill=BOTH)
#Label(win, text='Hello conteiner world').pack(side=TOP)
Button(win, text='Hello', command=greeting).pack(side=LEFT, anchor=N, fill=Y)
Label(win, text='Hello conteiner world').pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT, expand=Y, fill=X)
#Label(win, text='Hello conteiner world').pack(side=TOP)

win.mainloop()
