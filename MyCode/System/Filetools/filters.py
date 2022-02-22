import sys

def filter_files(name, function):
    input = open(name, 'r')     # создать объекты файлов
    output = open(name + '.out', 'w')   # выходной файл
    for line in input:
        output.write(function(line))    # записать изменную строку
    input.close()
    output.close()

def filter_stream(function):
    while True:
        line = sys.stdin.readline()
        if not line: break
        print(function(line), end = '')

if __name__ == '__mane__':
    filter_stream(lambda line: line)
