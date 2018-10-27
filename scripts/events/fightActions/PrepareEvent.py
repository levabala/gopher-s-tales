from scripts.events.EndDayEvent import EndDayEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import SleepTexts


def PrepareEvent(w):
  return EventTrivialFunc(
      w,
      SleepTexts,
      lambda w: (w, EndDayEvent)
  )
