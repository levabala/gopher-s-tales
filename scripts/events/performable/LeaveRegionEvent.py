from scripts.WorldMethods import getArea
from scripts.EventPipe import EventPipe
from scripts.events.MoveEvent import MoveEvent
from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import isPointerValid
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showMap
from texts.events import EmptyTexts
from scripts.structures.Point import Point


def LeaveRegionEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  # TODO: entering from different sides
  w = w._replace(currentAreaPointer=None)

  showMap(w)

  return (w, None)
