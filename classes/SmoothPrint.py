from multiprocessing import Process, Manager
import time
import atexit
from classes.Constants import SMALL_DELAY, MEDIUM_DELAY, BIG_DELAY

manager = Manager()
__toPrint__ = manager.list()


def smoothPrint(string='', delay=MEDIUM_DELAY):
  print(string)
  time.sleep(delay)


# here i've tried to implement it more complex way :))
'''
def smoothPrint(string=''):
  __toPrint__.append(string)


def tryPrintFirstForever(toPrint, plug):
  lastTime = time.clock()

  while True:
    nowTime = time.clock()
    time.sleep(0.3)
    # print(toPrint)
    if not toPrint or (nowTime - lastTime) * 1000 < SMOOTH_PRINT_DELAY:
      continue

    lastTime = nowTime

    string = toPrint.pop(0)
    print(string)


def killProcess():
  __tickHandleProcess__.terminate()


__tickHandleProcess__ = Process(target=tryPrintFirstForever, args=(__toPrint__, None))
__tickHandleProcess__.start()
atexit.register(killProcess)
'''
