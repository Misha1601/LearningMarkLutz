import sys                              # или sorted(sys.stdin)
lines = sys.stdin.readlines()           # читает входные строки из stdin,
lines.sort()                            # сортирует их
for line in lines: print(line, end='')  # отправляет результат в stdout
                                        # для дальнейшей обработки
