from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import FinishGame


def FinishGameEvent(w):
  return EventTrivialFunc(
      w,
      FinishGame,
      lambda w: (w, None)
  )
