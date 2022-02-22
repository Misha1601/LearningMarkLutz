"""
4 демонстрационных класса, выполняемые как низависимые процессы: команды;
если теперь одно окно будет завершено щелчком на кнопке Quit, остальные
продолжат работу; в данно случае не существует простого способавызвать все
методы report (впрочем, для организации взаимодействия между процессами можно
было бы воспользоваться сокетами и каналами), а кроме того, некоторые способы
запуска могут сбрасывать поток stdout дочерних программ и разрывать связь между
родителем и потомком;
"""
from tkinter import *
from launchmodes import PortableLauncher
demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

for demo in demoModules:
    PortableLauncher(demo, demo+'.py')()

root = Tk()
root.title('Processes')
Label(root, text='Nultiple program demo: command lines', bg='white').pack()
root.mainloop()
