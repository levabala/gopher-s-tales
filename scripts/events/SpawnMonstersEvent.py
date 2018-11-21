from random import random
from scripts.EventPipe import EventPipe
from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import forEachArea
from scripts.structures.AliveMonster import AliveMonster
from scripts.visual.SmoothPrint import smoothPrint
import texts.events.EmptyTexts as EmptyTexts


def SpawnMonstersEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  w = w._replace(monstersInTheWorld=[])

  global count
  count = 0

  def trySpawnMonster(w, area, path):
    if 'monster type' in area and random() < area['monster generate chance']:
      global count

      constructor = area['monster type']
      monster = AliveMonster(monster=constructor, state=constructor.init(), locationPath=path)
      w.monstersInTheWorld.append(monster)

      count += 1

  forEachArea(lambda area, path: trySpawnMonster(w, area, path), w.regions)

  smoothPrint('Monsters alive today: {}'.format(count))

  return (w, None)
