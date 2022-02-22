def scanner(name, function):
    file = open(name, 'r')      # создать обект файла
    while True:
        line = file.readline()  # вызов методов файла
        if not line: break      # до конца файла
        function(line)          # вызвать объект функции
    file.close()
