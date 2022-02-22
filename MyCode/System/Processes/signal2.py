"""
установка сигнала по истечении времени ожиданияи их обработка на языке Python;
функция time.sleep некорректно ведет себя при появлении сигнала SIGALARM
(как и любого другого сигнала на моем компьютере, работающим под управлением
Linux), поэтому здесьвызывается функция signal.pause, которая приостанавливает
выполнение сценария до появления сигнала;
"""

import sys, signal, time
def now(): return time.asctime()

def onSignal(signum, stackframe):           # обработчик сигнала
    print('Go alarm', signum, 'at', now())  # большинство обработчиков
                                            # остаются действующими
while True:
    print('Satting at', now())
    signal.signal(signal.SIGALRM, onSignal) # установить обработчик сигнала
    signal.alarm(5)                         # послать сигнал через 5 секунд
    signal.pause()                          # ждать сигнала
