from classes.Assets import d20
from classes.Constants import *
from classes.GopherVisual import (
    printCriticalFailure,
    printCriticalSuccess,
    printFailure,
    printSuccess
)


def floodEvent(gopher):
  print('\nOhhhh! FLOODING!!!')
  d = d20() + FLOOD_EVENT_ESCAPE_COEFF * gopher.agility

  if d < FLOOD_EVENT_FAILURE_CRIT_BOUND:
    printCriticalFailure()
    return gopher
  elif d < FLOOD_EVENT_FAILURE_SIMPLE_BOUND:
    printFailure()
    return gopher
  elif d < FLOOD_EVENT_SUCCESS_SIMPLE_BOUND:
    printSuccess()
    return gopher

  # should be never
  raise Exception('very strange dice')


def downFallEvent(gopher):
  print('\nOhhhh! DOWNFALL!!!')
  # do smth with gohper
  return gopher
