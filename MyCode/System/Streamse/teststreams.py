#!/usr/bin/env python3
"читает числа до символа конца файла и выводит их квадраты"
def interact():
    print('Hello world!') #  print выводит в sys.stdout
    while True:
        try:
            reply = input('Enter a number>') # input читает из sys.stdin
        except EOFError:
            break   # исключение при встрече символа EOF
        else:       # входные данные в виде строки
            num = int(reply)
            print("%d squared is %d" % (num, num**2))
    print('Bye')

if __name__ == '__main__':
    interact()      # если выполлняется, а не импортируется
