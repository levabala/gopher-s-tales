from copy import deepcopy
from scripts.visual.SmoothPrint import smoothPrint
from scripts.WorldMethods import getArea, getMonstersInLocation, getCurrentArea, getCurrentRegion
from scripts.EventPipe import EventPipe
from scripts.visual.Methods import (
    showMap, showThings, showStory,
    showProps, showCharacter, showLifeProps,
    showChangedProps
)
from scripts.GopherMethods import spendActionPoint
from scripts.Constants import SMALL_DELAY
from texts import areas

# possible events
from scripts.events.performable.MoveNorthEvent import MoveNorthEvent
from scripts.events.performable.MoveEastEvent import MoveEastEvent
from scripts.events.performable.MoveSouthEvent import MoveSouthEvent
from scripts.events.performable.MoveWestEvent import MoveWestEvent
from scripts.events.performable.LeaveRegionEvent import LeaveRegionEvent
from scripts.events.performable.EquipItemEvent import EquipItemEvent
from scripts.events.performable.UnequipItemEvent import UnequipItemEvent
from scripts.events.performable.ShowThingEvent import ShowThingEvent
from scripts.events.performable.FastMoveEvent import FastMoveEvent
from scripts.events.performable.ShowLegendEvent import ShowLegendEvent


def RootArea(): return {
    'move': lambda w: EventPipe(w, FastMoveEvent),
    'move north': lambda w: EventPipe(w, MoveNorthEvent),
    'move east': lambda w: EventPipe(w, MoveEastEvent),
    'move south': lambda w: EventPipe(w, MoveSouthEvent),
    'move west': lambda w: EventPipe(w, MoveWestEvent),
    'die': lambda w: w._replace(g=w.g._replace(alive=False)),
    'inventory': showThings,
    'actions': showActions,
    'map': showMap,
    'all props': showProps,
    'life props': showLifeProps,
    'character': showCharacter,
    'leave region': lambda w: EventPipe(w, LeaveRegionEvent),
    'equip': lambda w: EventPipe(w, EquipItemEvent),
    'unequip': lambda w: EventPipe(w, UnequipItemEvent),
    'thing': lambda w: EventPipe(w, ShowThingEvent),
    # 'help': help,
    'wait': wait,
    'show legend': lambda w: EventPipe(w, ShowLegendEvent),
    'look around': showDescription,
}


def showDescription(w):
  area = getCurrentArea(w)
  region = getCurrentRegion(w)

  if 'custom descriptions' in region:
    if not area['symbol'] in region['custom descriptions']:
      smoothPrint('No description here..')
      return w

    showStory(region['custom descriptions'][area['symbol']])
    return w

  if not area['symbol'] in areas.DESCRIPTIONS:
    smoothPrint('No description here..')
  else:
    showStory(areas.DESCRIPTIONS[area['symbol']])

  return w


def checkForMonsters(w):
  monsters = getMonstersInLocation(w, w.locationPath)
  if monsters:
    print('Here are {}'.format(', '.join([m.state.name for m in monsters])))

  return w


def eat(w):
  showStory('You eat magic food :)', True)
  gopherBefore = deepcopy(w.g)
  w = w._replace(
      g=w.g._replace(
          weight=w.g.weight + 0.5,
          actionPoints=w.g.actionPoints - 1
      )
  )
  showChangedProps(gopherBefore, w.g)

  return w


def wait(w):
  gopherBefore = deepcopy(w.g)
  w = w._replace(g=w.g._replace(stamina=0))
  showChangedProps(gopherBefore, w.g)

  return w


def help(w):
  showStory('Nothing here yet', True)
  return w


def showActions(w):
  area = getArea(w, w.currentAreaPointer)

  smoothPrint('Available actions:')
  for key in sorted(area.keys()):
    smoothPrint('  ' + key, delay=SMALL_DELAY)
  print()
  return w
