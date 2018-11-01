from scripts.EventPipe import EventPipe
from scripts.events.MoveEvent import MoveEvent
from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import isPointerValid
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showMap, showEquipment, showStory, showThings
from scripts.GopherMethods import isTypeInEquipement, unequipItem
from texts.events import EmptyTexts
from scripts.structures.Point import Point


def UnequipItemEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  def nextPlease(w):
    showStory('Invalid index', raw=True)
    print()

    return (w, UnequipItemEvent)

  if not w.g.equipement:
    smoothPrint('You have nothing equiped')
    return (w, None)

  showEquipment(w)
  print()

  mess = 'Enter item to equip index: '

  num = input(mess)
  print()

  if not num.isdigit():
    if num == 'abort':
      return (w, None)
    return nextPlease(w)

  num = int(num) - 1

  if (
      (num < 0) or
      (num > len(w.g.equipement) - 1)
  ):
    return nextPlease(w)

  w = w._replace(g=unequipItem(w.g, num))

  showThings(w)

  return (w, None)
