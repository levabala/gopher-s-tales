from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import isPointerValid
from scripts.visual.SmoothPrint import smoothPrint
from texts.events import EmptyTexts


def MoveEastEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  nowPointer = w.currentAreaPointer
  newPointer = nowPointer._replace(x=nowPointer.x + 1)
  if isPointerValid(w, newPointer):
    return (w._replace(currentAreaPointer=newPointer), None)
  else:
    smoothPrint('You can\'t move this direction')
    return (w, None)
