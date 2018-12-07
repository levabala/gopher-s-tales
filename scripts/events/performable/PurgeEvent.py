from random import randint
from scripts.WorldMethods import getCurrentArea, getMonstersInLocation
from scripts.events.Event import EventTrivialFunc
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showStory
from texts.events import PurgeTexts

from scripts.events.FightEvent import FightEvent
from scripts.monsters.SlugMonster import SlugMonster


def PurgeEvent(w):
  return EventTrivialFunc(
      w,
      PurgeTexts,
      _process
  )


def _process(w):
  monsters = getMonstersInLocation(w, w.locationPath)

  if not monsters:
    showStory('No monsters here!', True)
    return (w, None)

  monsterToFight = monsters[randint(0, len(monsters) - 1)]

  return (w._replace(enemyType=monsterToFight.monster, enemyState=monsterToFight.state), FightEvent)
