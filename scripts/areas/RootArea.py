from scripts.visual.SmoothPrint import smoothPrint
from scripts.WorldMethods import getArea
from scripts.EventPipe import EventPipe
from scripts.visual.Methods import showMap, showThings
from scripts.Constants import SMALL_DELAY

# possible events
from scripts.events.performable.MoveNorthEvent import MoveNorthEvent
from scripts.events.performable.MoveEastEvent import MoveEastEvent
from scripts.events.performable.MoveSouthEvent import MoveSouthEvent
from scripts.events.performable.MoveWestEvent import MoveWestEvent
from scripts.events.performable.LeaveRegionEvent import LeaveRegionEvent
from scripts.events.performable.EquipItemEvent import EquipItemEvent
from scripts.events.performable.UnequipItemEvent import UnequipItemEvent


def RootArea(): return {
    'go north': lambda w: EventPipe(w, MoveNorthEvent),
    'go east': lambda w: EventPipe(w, MoveEastEvent),
    'go south': lambda w: EventPipe(w, MoveSouthEvent),
    'go west': lambda w: EventPipe(w, MoveWestEvent),
    'die': lambda w: w._replace(g=w.g._replace(alive=False)),
    'inventory': showThings,
    'actions': showActions,
    'map': showMap,
    'leave region': lambda w: EventPipe(w, LeaveRegionEvent),
    'equip': lambda w: EventPipe(w, EquipItemEvent),
    'unequip': lambda w: EventPipe(w, UnequipItemEvent),
}


def showActions(w):
  area = getArea(w, w.currentAreaPointer)

  smoothPrint('Available actions:')
  for key in sorted(area.keys()):
    smoothPrint('  ' + key, delay=SMALL_DELAY)
  print()
  return w
