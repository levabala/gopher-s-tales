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

  num = w.itemSwitchIndex

  item = w.g.inventory[num]
  t = item['type']
  equipement = sorted(w.g.equipement, key=lambda el: el['name'])
  if isTypeInEquipement(w.g, t):
    # unequip the first (and alone) item of the same type
    index = 0
    for it in equipement:
      if it['type'] == t:
        gopherAfter = unequipItem(w.g, index)
        w = w._replace(g=gopherAfter)
        break
      index += 1

  inventory = sorted(w.g.inventory, key=lambda el: el['name'])
  gen = (
      i for i in range(len(inventory))
      if inventory[i]['id'] == item['id']
  )
  index = next(gen)
  w = w._replace(
      g=equipItem(
          w.g,
          index
      )
  )

  showThings(w)

  return (w, None)
