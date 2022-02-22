import os
print('setenv...') #, end=' ')
print(os.environ['USER'])   # выведет текущее значение переменной оболочки

os.environ['USER'] = 'Brain'     # неявно вызовет функцию os.putenv
os.system('python echoenv.py')

os.environ['USER'] = 'Arthur' # изменение передается порожденным программам
os.system('python echoenv.py') # и связанным с процессом библ. модулям на С

os.environ['USER'] = input('?')
print(os.popen('python echoenv.py').read())
