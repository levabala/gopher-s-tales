from scripts.EventPipe import EventPipe
from scripts.events.MoveEvent import MoveEvent
from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import isPointerValid
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showMap, showInventory, showEquipment, showStory, showThings
from scripts.GopherMethods import isTypeInEquipement, equipItem, unequipItem
from texts.events import EmptyTexts
from scripts.structures.Point import Point


def SwitchItemEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  def nextPlease(w):
    showStory('Invalid index', raw=True)
    print()

    return (w, SwitchItemEvent)

  num = w.itemSwitchIndex

  t = w.g.inventory[num]['type']
  if isTypeInEquipement(w.g, t):
    # unequip the first (and alone) item of the same type
    index = 0
    for item in w.g.equipement:
      if item['type'] == t:
        gopherAfter = unequipItem(w.g, index)
        w = w._replace(g=gopherAfter)
        break

  w = w._replace(g=equipItem(w.g, num))

  showThings(w)

  return (w, None)
