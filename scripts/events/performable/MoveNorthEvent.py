from scripts.EventPipe import EventPipe
from scripts.events.MoveEvent import MoveEvent
from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import isPointerValid
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showMap
from texts.events import EmptyTexts
from scripts.structures.Point import Point


def MoveNorthEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      lambda w: (w._replace(moveDelta=Point(0, -1)), MoveEvent)
  )
