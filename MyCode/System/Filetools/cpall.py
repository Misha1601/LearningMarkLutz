"""
################################################################################
Порядок использования: "python3 cpall.py dirFrom dirTo".
Рекурсивно копируем дерево каталогов. Действует подобно команде Unix "cp -r
dirFrom/* dirTo", предпологая, что оба аргумента dirFrom и dirTo являются
именами каталогов.
Был написан с целью обойти фатальные ошибки при копировании файлов
перетаскиванием мыши в Windows (когда встреча первого же проблемного файла
вызывает прекращение операции копирования) и обеспечить возможность реализации
более специализированных операций копирования на языке Python.
################################################################################
"""
import os, sys
maxfileload = 1000000
blksize = 1024 * 500

def copyfile(pathFrom, pathTo, maxfileload=maxfileload):
    """
    копирует один файл из pathFrom в pathTo, байт в байт;
    использует двоичный режим для подавления операций
    кодирования/декодирования и преобразования символов конца строки
    """
    if os.path.getsize(pathFrom) <= maxfileload:
        bytesFrom = open(pathFrom, 'rb').read() # маленький файл читать целиком
        open(pathTo, 'wb').write(bytesFrom)
    else:
        fileFrom = open(pathFrom, 'rb')           # большие файлы - по частям
        fileTo   = open(pathTo,   'wb')             # режим b для обоих файлов
        while True:
            bytesFrom = fileFrom.read(blksize)  # прочитать очередной блок
            if not bytesFrom: break             # пустой после последнего блока
            fileTo.write(bytesFrom)

def copytree(dirFrom, dirTo, verbose=0):
    """
    Копирует содержимое dirFrom и вложенные подкаталоги в dirTo,
    возвращает счетчики (files, dirs);
    для представления имен каталогов , недекодируемых на других платформах,
    может потребоваться использовать переменные типа bytes;
    в Unix может потребоваться выполнить дополнительные проверки типов файлов,
    чтобы пропускать ссылки, файлы fifo и так далее.
    """
    fcount = dcount = 0
    for filename in os.listdir(dirFrom):
        pathFrom = os.path.join(dirFrom, filename)
        pathTo   = os.path.join(dirTo, filename)
        if not os.path.isdir(pathFrom):
            try:
                if verbose > 1: print('copying', pathFrom, 'to', pathTo)
                copyfile(pathFrom, pathTo)
                fcount += 1
            except:
                print('Error copying', pathFrom, 'to', pathTo, '--skipped')
                print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            if verbose: print('copying dir', pathFrom, 'to', pathTo)
            try:
                os.mkdir(pathTo)    # создать новый подкаталог
                below = copytree(pathFrom, pathTo) # спуск в подкаталоги
                fcount += below[0]  # увеличить счетчики
                dcount += below[1]  # подкаталогов
                dcount += 1
            except:
                print('Error creating', pathTo, '--skipped')
                print(sys.exc_info()[0], sys.exc_info()[1])
    return (fcount, dcount)

def getargs():
    """
    извлекает и проверяет аргументы с именами каталогов, по умолчанию
    возвращает None в случае ошибки
    """
    try:
        dirFrom, dirTo = sys.argv[1:]
    except:
        print('Usage error: cpall.py dirFrom dirTo')
    else:
        if not os.path.isdir(dirFrom):
            print('Error: dirFrom is not a directory')
        elif not os.path.exists(dirTo):
            os.mkdir(dirTo)
            print('Note: dirTo was created')
            return (dirFrom, dirTo)
        else:
            print('Warning: dirTo already exists')
            if hasattr(os.path, 'samefile'):
                same = os.path.samefile(dirFrom, dirTo)
            else:
                same = os.path.abspath(dirFrom) == os.path.abspath(dirTo)
            if same:
                print('Error: dirFrom same as dirTo')
            else:
                return (dirFrom, dirTo)

if __name__ == '__main__':
    import time
    dirstuple = getargs()
    if dirstuple:
        print('Copying...')
        start = time.clock()
        fcount, dcount = copytree(*dirstuple)
        print('Copied', fcount, 'files', dcount, 'directories', end=' ')
        print('in', time.clock() - start, 'seconds')
