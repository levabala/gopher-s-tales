from scripts.events.BornEvent import BornEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import StartGameTexts


def StartGameEvent(w):
  return EventTrivialFunc(
      w,
      StartGameTexts,
      lambda w: (w, BornEvent)
  )
