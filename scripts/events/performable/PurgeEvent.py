from scripts.WorldMethods import getArea
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
  area = getArea(w, w.currentAreaPointer)
  if not 'monsters count' in area or area['monsters count'] == 0:
    showStory('No monsters here!')
    return (w, None)

  monstersType = area['monsters type']
  showStory(
      'People say that here are about {} {}'.format(
          area['monsters count'],
          monstersType.textModule.MANY_NAME,
      ),
      True
  )

  return (w._replace(enemyType=monstersType), FightEvent)
