"""
Отыскивает наибольший файл с исходным программным кодом на языке Python
в единственном каталоге.
Поиск выполняется в каталоге стандартной библиотеки Python для Windows, если
в аргументе командной строки не был указан какой то другой каталог.
"""
import os, sys, glob
dirname = r'/home/misha/Python/System/Filetools' if len(sys.argv) == 1 else sys.argv[1]
allsize = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsize.append((filesize, filename))

allsize.sort()
print(allsize[:2])
print(allsize[-2:])
