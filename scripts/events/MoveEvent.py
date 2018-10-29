from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import isPointerValid
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showMap
from scripts.WorldMethods import getRegion
from texts.events import EmptyTexts


def MoveEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _processRegionMoving
      if w.currentAreaPointer is None
      else _processAreaMoving
  )

# TODO: optimize this shit


def _processRegionMoving(w):
  nowPointer = w.currentRegionPointer
  newPointer = nowPointer._replace(
      x=nowPointer.x + w.moveDelta.x,
      y=nowPointer.y + w.moveDelta.y,
  )

  if isPointerValid(w, newPointer, w.regions):
    w = w._replace(currentRegionPointer=newPointer)
    showMap(w)
    return (w, None)
  else:
    smoothPrint('You can\'t move this direction')
    return (w, None)


def _processAreaMoving(w):
  currentRegion = getRegion(w, w.currentRegionPointer)

  nowPointer = w.currentAreaPointer
  newPointer = nowPointer._replace(
      x=nowPointer.x + w.moveDelta.x,
      y=nowPointer.y + w.moveDelta.y,
  )

  if isPointerValid(w, newPointer, currentRegion['areas']):
    w = w._replace(currentAreaPointer=newPointer)
    showMap(w)
    return (w, None)
  else:
    smoothPrint('You can\'t move this direction')
    return (w, None)
