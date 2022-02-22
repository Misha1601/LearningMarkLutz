#!/usr/bin/env python3
"""
объекты, похожие на файлы, один из которых сохраняет в строке текст,
отправленный в стандартный поток ввода, а другой обеспечивает ввод текста
из строки в станндартный поток ввода; функция redirect вызывает переданную
ей функцию, для которой стандартные потоки ввода и выводабудут связаны
с объектами, похожими на файлы;
"""
import sys                          # импортировать встроенный модуль

class Output:                       # имитирует входной файл
    def __init__(self):
        self.text=''                # при создании строка пустая
    def write(self, string):        # добавляет строку байтов
        self.text += string
    def writelines(self, lines):    # добавляет все строки в список
        for line in lines: self.write(line)

class Input:                        # имитирует входной файл
    def __init__(self, input=''):   # аргумент по умолчанию
        self.text = input           # сохраняет строку при создании
    def read(self, size = None):    # необязательный аргумент
        if size == None:            # прочитать N байт или все
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:eoln+1], self.text[size:]
        return res
    def readline(self):
        eoln = self.text.find('\n')     # найти смещение следующего eoln
        if eoln == -1:                  # извлечь строку из eoln
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:eoln+1], self.text[eoln+1:]
        return res

def redirect(function, pargs, kargs, input):    # перенаправляет stdin/out
    savestreams = sys.stdin, sys.stdout         # вызывает объект функции
    sys.stdin = Input(input)                    # возвращает текств stdout
    sys.stdout = Output()
    try:
        result = function(*pargs, **kargs)      # вызывает функцию с аргументами
        output = sis.stdout.text
    finally:                                    # восстановить, независимо от
        sys.stdin, sys.stdout = savestreams     # того, было ли исключение
    return(result, output)                      # вернуть результат,
                                                # если исключения небыло
