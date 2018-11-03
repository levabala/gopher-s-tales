from scripts.EventPipe import EventPipe
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
  return (EventPipe(w, UserActionEvent), None)
