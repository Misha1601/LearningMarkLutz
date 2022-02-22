#!/usr/bin/env python3
"""
разбиваем сроку или текстовый файл на страницы для интерактивного просмотра
"""

def more(text, numlines=15):
    lines=text.splitlines()     # подобно split('\n') но без '' в конце
    while lines:
        chunk=lines[:numlines]
        lines=lines[numlines:]
        for line in chunk: print(line)
        if lines and input('More?') not in ['y', 'Y']: break

if __name__ == '__main__':               # если выполняется, а не импортируется 
#    import sys                          # если запускается как сценарий
#    more(open(sys.argv[1]).read(), 10)   # отобразить построчно содержимое файла, указанного в командной строке
    import sys
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())
