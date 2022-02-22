import sys
sum = 0
while True:
    try:
        line = input()      # или sys.stdin.readlines()
    except EOFError:        # или for line in sys.stdin:
        break               # input отсекает символы \n конца строки
    else:
        sum += int(line)    # во втором издании использовалась функция sting.atoi()
print(sum)
