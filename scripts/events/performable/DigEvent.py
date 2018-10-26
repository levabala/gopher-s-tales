from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import DigTexts


def DigEvent(w):
  return EventTrivialFunc(
      w,
      DigTexts,
      lambda w: (w, None)
  )
