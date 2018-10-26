from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import EnterMarketTexts


def EnterMarketEvent(w):
  return EventTrivialFunc(
      w,
      EnterMarketTexts,
      lambda w: (w, None)
  )
