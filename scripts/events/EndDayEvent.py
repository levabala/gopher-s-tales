from scripts.events.Event import EventTrivialFunc
from texts.events import EndDayTexts


def EndDayEvent(w):
  return EventTrivialFunc(
      w,
      EndDayTexts,
      lambda w: (w, None)
  )
