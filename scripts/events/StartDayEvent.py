from scripts.EventPipe import EventPipe
from scripts.events.MidwayEvent import MidwayEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import StartDayTexts


def StartDayEvent(w):
  return EventTrivialFunc(
      w,
      StartDayTexts,
      _process
  )


def _process(w):
  while w.g.alive:
    w = w._replace(g=w.g._replace(actionPoints=3))
    w = EventPipe(w, MidwayEvent)
  return (w, None)
