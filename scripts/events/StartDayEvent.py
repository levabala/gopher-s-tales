from scripts.EventPipe import EventPipe
from scripts.events.MidwayEvent import MidwayEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import StartDayTexts
from scripts.events.DieEvent import DieEvent
from scripts.events.WinGameEvent import WinGameEvent
from scripts.GopherMethods import isDead, isWinner
from scripts.visual.Methods import smoothPrint
from scripts.events.SleepEvent import SleepEvent
from scripts.events.SpawnMonstersEvent import SpawnMonstersEvent


def StartDayEvent(w):
  return EventTrivialFunc(
      w,
      StartDayTexts,
      _process
  )


def _process(w):
  w = w._replace(days=w.days + 1)
  smoothPrint('\n--- DAY {} ---\n'.format(w.days))

  w = EventPipe(w, SpawnMonstersEvent)
  w = EventPipe(w, MidwayEvent)

  if isDead(w.g):
    return (w, DieEvent)

  if isWinner(w.g):
    return (w, WinGameEvent)

  return (EventPipe(w, SleepEvent), StartDayEvent)
