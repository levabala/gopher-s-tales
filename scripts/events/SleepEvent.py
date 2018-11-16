from copy import deepcopy
from scripts.events.EndDayEvent import EndDayEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import SleepTexts
from scripts.Constants import SLEEP_CHANGES, BAD_SLEEP_CHANGES
from scripts.structures.Gopher import Gopher
from scripts.visual.Methods import showChangedProps, showStory
from scripts.GopherMethods import normalizeProps
from scripts.WorldMethods import getCurrentArea


def SleepEvent(w):
  return EventTrivialFunc(
      w,
      SleepTexts,
      _process,
  )


def _process(w):
  input('Press Enter to sleep...')

  gopherBefore = deepcopy(w.g)

  g = w.g._asdict()

  area = getCurrentArea(w)
  if area['area name'] == 'Hole':
    for prop in SLEEP_CHANGES:
      g[prop] += SLEEP_CHANGES[prop]
    showStory('You had a nice sleep', True)
  else:
    for prop in BAD_SLEEP_CHANGES:
      g[prop] += BAD_SLEEP_CHANGES[prop]
    showStory('You had a bad sleep (you slept outside your hole)', True)

  w = w._replace(g=Gopher(**g))

  w = normalizeProps(w)
  showChangedProps(gopherBefore, w.g)

  return (w, EndDayEvent)
