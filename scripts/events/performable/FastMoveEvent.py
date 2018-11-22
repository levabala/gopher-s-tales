import time
import getch
import sys
from termios import tcflush, TCIFLUSH
from scripts.WorldMethods import getArea, getCurrentRegion, getCurrentArea
from scripts.EventPipe import EventPipe
from scripts.events.Event import EventTrivialFunc
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showMap, moveUpCursor
from texts.events import EmptyTexts

from scripts.events.performable.EnterRegionEvent import EnterRegionEvent
from scripts.events.performable.MoveNorthEvent import MoveNorthEvent
from scripts.events.performable.MoveEastEvent import MoveEastEvent
from scripts.events.performable.MoveSouthEvent import MoveSouthEvent
from scripts.events.performable.MoveWestEvent import MoveWestEvent


def FastMoveEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  smoothPrint('Use WASD to move across the map and')
  smoothPrint('use E to enter location (any other key will exit this mode)')
  print()

  m = {
      'd': MoveEastEvent,
      'w': MoveNorthEvent,
      'a': MoveWestEvent,
      's': MoveSouthEvent,
  }

  tcflush(sys.stdin, TCIFLUSH)

  area = getCurrentArea(w)
  if 'areas' in area:
    m['e'] = EnterRegionEvent

  showMap(w)
  k = getch.getch().lower()
  w = w._replace(fastMoveMode=True)
  while k in m and w.g.stamina > 0:

    w = EventPipe(w, m[k])
    region = getCurrentRegion(w)['areas']
    height = len(region) + 4
    moveUpCursor(height)
    showMap(w, True)

    area = getCurrentArea(w)
    if 'areas' in area:
      m['e'] = EnterRegionEvent
    elif 'e' in m:
      del m['e']

    k = getch.getch().lower()

  w = w._replace(fastMoveMode=False)

  return (w, None)
