from scripts.EventPipe import EventPipe
from scripts.events.MidwayEvent import MidwayEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import StartDayTexts
from scripts.events.DieEvent import DieEvent
from scripts.events.WinGameEvent import WinGameEvent
from scripts.GopherMethods import isDead, isWinner
from scripts.visual.Methods import smoothPrint


def StartDayEvent(w):
  return EventTrivialFunc(
      w,
      StartDayTexts,
      _process
  )


def _process(w):
  w = w._replace(days=w.days + 1)
  smoothPrint('\n--- DAY {} ---\n'.format(w.days))

  if not w.g.alive:
    return (w, None)

  w = w._replace(g=w.g._replace(actionPoints=3))
  w = EventPipe(w, MidwayEvent)

  if isDead(w.g):
    return (w, DieEvent)

  if isWinner(w.g):
    return (w, WinGameEvent)

  return (w, StartDayEvent)
