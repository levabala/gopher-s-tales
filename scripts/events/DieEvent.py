from scripts.events.FinishGameEvent import FinishGameEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import DieTexts


def DieEvent(w):
  return EventTrivialFunc(
      w,
      DieTexts,
      lambda w: (w._replace(g=w.g._replace(alive=False)), FinishGameEvent)
  )
