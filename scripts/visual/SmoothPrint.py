import time
from scripts.Constants import SMALL_DELAY, MEDIUM_DELAY, BIG_DELAY


def smoothPrint(string='', delay=MEDIUM_DELAY):
  print(string)
  time.sleep(delay)
