from scripts.WorldMethods import getArea
from scripts.events.Event import EventTrivialFunc
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showStory
from texts.events import PurgeTexts

from scripts.events.FightEvent import FightEvent
from scripts.monsters import SlugMonster


def PurgeEvent(w):
  return EventTrivialFunc(
      w,
      PurgeTexts,
      _process
  )


def _process(w):
  area = getArea(w, w.currentAreaPointer)
  if not 'monsters count' in area or area['monsters count'] == 0:
    showStory('No monsters here!')
    return (w, None)

  return (w._replace(enemyType=SlugMonster), FightEvent)
