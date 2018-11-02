from copy import deepcopy
from scripts.events.EndDayEvent import EndDayEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import SleepTexts
from scripts.Constants import SLEEP_CHANGES
from scripts.structures.Gopher import Gopher
from scripts.visual.Methods import showChangedProps
from scripts.GopherMethods import normalizeProps


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
  for prop in SLEEP_CHANGES:
    g[prop] += SLEEP_CHANGES[prop]

  w = w._replace(g=Gopher(**g))

  w = normalizeProps(w)
  showChangedProps(gopherBefore, w.g)

  return (w, EndDayEvent)
