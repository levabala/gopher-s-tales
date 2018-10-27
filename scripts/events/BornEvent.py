from scripts.events.StartDayEvent import StartDayEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import BornTexts


def BornEvent(w):
  return EventTrivialFunc(
      w,
      BornTexts,
      lambda w: (w, StartDayEvent)
  )
