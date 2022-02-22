"""
Отыскивает наибольший файл с исходным программным кодом на языке Python в дереве каталогов.
Поиск выполняется в каталоге стандарной бибилиотеки, отображение результатов
выполняется с помощью модуля pprint.
"""
import sys, os, pprint
trace = False
if sys.platform.startswith('win'):
    dirname = r'C:\Python31\Lib'
else:
    dirname = r'/usr/lib/python3.7'

allsize = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsize.append((fullsize, fullname))
allsize.sort()
pprint.pprint(allsize[:2])
pprint.pprint(allsize[-2:])
