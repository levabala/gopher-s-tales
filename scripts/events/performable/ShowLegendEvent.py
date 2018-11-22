from scripts.WorldMethods import getArea
from scripts.EventPipe import EventPipe
from scripts.events.MoveEvent import MoveEvent
from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import isPointerValid
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showThingProps, showThings, showStory
from texts.events import EmptyTexts
from scripts.structures.Point import Point


def ShowLegendEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  
  
  return (w, None)
