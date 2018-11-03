from copy import deepcopy
from scripts.events.EndDayEvent import EndDayEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import WinGameTexts
from scripts.Constants import SLEEP_CHANGES
from scripts.structures.Gopher import Gopher
from scripts.visual.Methods import showChangedProps
from scripts.GopherMethods import normalizeProps


def WinGameEvent(w):
  return EventTrivialFunc(
      w,
      WinGameTexts,
      lambda w: (w, None),
  )
