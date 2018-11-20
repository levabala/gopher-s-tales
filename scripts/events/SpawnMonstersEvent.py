from scripts.EventPipe import EventPipe
from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import forEachArea
import texts.events.EmptyTexts as EmptyTexts


def SpawnMonstersEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  print('SPAWN')
  forEachArea(lambda area: print(area['name']), w.regions)
