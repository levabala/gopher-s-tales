from scripts.EventPipe import EventPipe
from scripts.events.MoveEvent import MoveEvent
from scripts.events.Event import EventTrivialFunc
from scripts.events.SwitchItemEvent import SwitchItemEvent
from scripts.WorldMethods import isPointerValid
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showMap, showInventory, showEquipment, showStory, showThings
from scripts.GopherMethods import isTypeInEquipement, equipItem, unequipItem
from texts.events import EmptyTexts
from scripts.structures.Point import Point


def EquipItemEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  def nextPlease(w):
    showStory('Invalid index', raw=True)
    print()

    return (w, EquipItemEvent)

  showInventory(w, True)
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
      (num > len(w.g.inventory) - 1)
  ):
    return nextPlease(w)

  t = w.g.inventory[num]['type']
  if isTypeInEquipement(w.g, t):
    showStory('You are trying to have to things of the same type equiped', True)

    msg = 'Enter action index:'
    msg += '\n1. switch item'
    msg += '\n2. change item to equip index\n'

    actionIndex = input(msg)
    print()

    if not actionIndex.isdigit():
      return nextPlease(w)

    actionIndex = int(actionIndex)

    if actionIndex != 1:
      return nextPlease(w)
    else:
      w = w._replace(itemSwitchIndex=num)
      return (w, SwitchItemEvent)

  w = w._replace(g=equipItem(w.g, num))

  showThings(w)

  return (w, None)
