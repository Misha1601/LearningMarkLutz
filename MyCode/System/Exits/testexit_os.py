#!/usr/bin/env python3

def outahere():
    import os
    print('Bye os world!')
    os._exit(99)
    print('Never reached')

if __name__ == '__main__': outahere()
