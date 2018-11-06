from scripts.events.EndDayEvent import EndDayEvent
from scripts.events.Event import EventTrivialFunc
from texts.events import SleepTexts

from scripts.Constants import HOLD_DURATION


def HoldEvent(w):
  return EventTrivialFunc(
      w,
      SleepTexts,
      lambda w: (w._replace(holdTurnsLeft=HOLD_DURATION), None)
  )
