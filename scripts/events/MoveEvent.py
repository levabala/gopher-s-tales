from scripts.events.Event import EventTrivialFunc
from scripts.visual.Methods import showMap
from scripts.visual.SmoothPrint import smoothPrint
from scripts.WorldMethods import getCurrentRegion, isPointerValid
from texts.events import EmptyTexts


def MoveEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _processAreaMoving
  )


def _processAreaMoving(w):
  currentRegion = getCurrentRegion(w)

  nowPointer = w.locationPath[-1]
  newPointer = nowPointer._replace(
      x=nowPointer.x + w.moveDelta.x,
      y=nowPointer.y + w.moveDelta.y,
  )

  if isPointerValid(w, newPointer, currentRegion['areas']):
    w = w._replace(locationPath=w.locationPath[:-1] + [newPointer])
    showMap(w)
    return (w, None)
  else:
    smoothPrint('You can\'t move this direction')
    return (w, None)
