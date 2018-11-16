from scripts.events.Event import EventTrivialFunc
from scripts.visual.Methods import showMap
from scripts.visual.SmoothPrint import smoothPrint
from scripts.WorldMethods import getCurrentRegion, isPointerValid, getCurrentArea
from texts.events import EmptyTexts

from scripts.events.SleepEvent import SleepEvent


def MoveEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _processAreaMoving
  )


def _processAreaMoving(w):
  currentRegion = getCurrentRegion(w)
  currentArea = getCurrentArea(w)

  nowPointer = w.locationPath[-1]
  newPointer = nowPointer._replace(
      x=nowPointer.x + w.moveDelta.x,
      y=nowPointer.y + w.moveDelta.y,
  )

  if isPointerValid(w, newPointer, currentRegion['areas']):
    w = w._replace(g=w.g._replace(stamina=w.g.stamina - currentArea['move cost']))
    w = w._replace(locationPath=w.locationPath[:-1] + [newPointer])
    if not w.fastMoveMode:
      showMap(w)

    return (w, None)
  else:
    if not w.fastMoveMode:
      smoothPrint('You can\'t move this direction')
    return (w, None)
