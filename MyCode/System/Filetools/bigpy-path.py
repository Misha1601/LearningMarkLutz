"""
Отыскивает наибольший файл с исходным программным кодом на языке Python,
присутствующие в пути поиска модулей.
Пропускает каталоги. которые уже были просканированы; нормализует пути и регистр
символов, обеспечивая корректность сравнения; включает в  выводимые результаты
счетчики строк. Здесь недостаточно использовать os.environ['PYTHONPATH']:
этот список является лишь подмножеством списка sys.path.
"""
import sys, os, pprint
trace = 1               # 1 -каталоги, 2 - файлы
visited = {}
allsizes = []
for srcdir in sys.path:
    for (thisDir, subsHere, filesHere) in os.walk(srcdir):
        if trace > 0: print(thisDir)
        thisDir = os.path.normpath(thisDir)
        fixcase = os.path.normpath(thisDir)
        if fixcase in visited:
            continue
        else:
            visited[fixcase] = True
        for filename in filesHere:
            if filename.endswith('.py'):
                if trace > 1: print('...', filename)
                pypath = os.path.join(thisDir, filename)
                try:
                    pysize = os.path.getsize(pypath)
                except os.error:
                    print('skipping', pypath, sys.exc_info()[0])
                else:
                    pylines = len(open(pypath, 'rb').readlines())
                    allsizes.append((pysize, pylines, pypath))
print('By size...')
allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])



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
