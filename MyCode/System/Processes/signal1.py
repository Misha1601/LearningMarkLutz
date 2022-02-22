"""
обаботка сигналов в Python; номер сигнала N передается как аргумент командной
строки; чтобы передать сигнал этому процессу, используйте коменду оболочки "kill
-N pid"; большинство обработчиков сигналов восстанавливаются интерпретатором
после обработки сигнала (смотрите главу, посвященную сетевым сценариям, где
приводится описание сигнала SIGCHLD);  в Windows модуль signal также доступен,
но он определяет небольшое количество типов сигналов, а кроме того, в Windows
отсутствует функция os.kill;
"""

import sys, signal,time
def now(): return time.ctime(time.time())   # строка с текущим времинем

def onSignal(signum, stackframe):           # обработчик сигнала
    print('Go signal', signum, 'at', now()) # большинство обработчиков
                                            # остаются действующими
signum = int(sys.argv[1])
signal.signal(signum, onSignal)             # установить обработчик сигнала
while True: signal.pause()                  # ждать сигнала (или: pass)