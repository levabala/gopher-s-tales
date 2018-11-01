from scripts.WorldMethods import getArea
from scripts.EventPipe import EventPipe
from scripts.events.MoveEvent import MoveEvent
from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import isPointerValid
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showThingProps, showThings, showStory
from texts.events import EmptyTexts
from scripts.structures.Point import Point


def ShowThingEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  def nextPlease(w):
    showStory('Invalid index', raw=True)
    print()

    return (w, ShowThingEvent)

  showThings(w)
  print()

  mess = 'Enter item to show index: '
  num = input(mess)
  print()

  if not num.isdigit():
    return nextPlease(w)

  num = int(num) - 1

  things = sorted(w.g.equipement + w.g.inventory, key=lambda el: el['name'])
  if (
      (num < 0) or
      (num > len(things) - 1)
  ):
    return nextPlease(w)

  showThingProps(things[num])

  return (w, None)
