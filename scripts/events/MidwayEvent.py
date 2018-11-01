from scripts.events.SleepEvent import SleepEvent
from scripts.events.UserActionEvent import UserActionEvent
from scripts.events.DieEvent import DieEvent

from scripts.events.Event import EventTrivialFunc
from scripts.GopherMethods import isDead
from texts.events import MidwayTexts


def MidwayEvent(w):
  return EventTrivialFunc(
      w,
      MidwayTexts,
      _process
  )


def _process(w):
  g = w.g

  # check if is dead
  if isDead(g):
    return (w, DieEvent)

  # check if can't do anymore
  if g.actionPoints == 0:
    return (w, SleepEvent)

  # if not dead and is active then
  return (w, UserActionEvent)
