from scripts.events.EndDayEvent import EndDayEvent
from scripts.events.Event import EventTrivialFunc
from scripts.visual.Methods import showStory, green
from texts.events import HoldTexts

from scripts.Constants import HOLD_DURATION, HOLD_EVASION_COEFF


def HoldEvent(w):
  return EventTrivialFunc(
      w,
      HoldTexts,
      _process,
  )


def _process(w):
  showStory('Now your evasion for {} multiplied by {}%'.format(
      green('light attacks'),
      green(round((HOLD_EVASION_COEFF - 1) * 100))
  ), True)

  return (w._replace(g=w.g._replace(holdTurnsLeft=HOLD_DURATION)), None)
