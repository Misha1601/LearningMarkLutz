#!/usr/local/bin/python3
from sys import argv
from scanfile import scanner
class UnknownCommand(Exception): pass

def processLine(line):      # определить функцию,
    if line[0] == '*':      # применяемую к каждой строке
        print("Ms.", line[1:-1])
    elif line[0] == '+':
        print("Mr.", line[1:-1])    # отбросить первый и последний символы
    else:
        raise UnknownCommander(line)        # возбудить исключение

filename = 'data.txt'
if len(argv) == 2: filename = argv[1]   # аргумент командной строки с именем
scanner(filename, processLine)          # файла запускает сканер
