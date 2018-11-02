from random import randint
from scripts.visual.ConsoleColors import green
from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventFunc
from scripts.Assets import showRollResult, rollDice
from scripts.Constants import (
    DIGGING_NORMAL_DEEP,
    DIGGING_EVENT_FAILURE_CRIT_BOUND,
    DIGGING_EVENT_FAILURE_SIMPLE_BOUND,
    DIGGING_EVENT_SUCCESS_SIMPLE_BOUND,
    DIGGING_EVENT_SUCCESS_SIMPLE_BOUND,
    LEVEL_DIGGING_COEFF,
    DIG_INTELLIGENCE_COEFF,
    DIG_STRENGTH_COEFF,
    YOU_STRING
)
from texts.events import DigTexts

# import possible events
from scripts.events.FloodEvent import FloodEvent
from scripts.events.DownfallEvent import DownfallEvent


def DigEvent(w):
  return EventFunc(
      w,
      lambda w: w,
      DigTexts,
      __calcDice__,
      DIGGING_EVENT_FAILURE_CRIT_BOUND,
      DIGGING_EVENT_FAILURE_SIMPLE_BOUND,
      DIGGING_EVENT_SUCCESS_SIMPLE_BOUND,
      DIGGING_EVENT_SUCCESS_SIMPLE_BOUND,
      lambda w: (w._replace(
          g=w.g._replace(actionPoints=0)
      ), FloodEvent if randint(0, 1) else DownfallEvent),
      lambda w: (w._replace(g=w.g._replace(
          actionPoints=w.g.actionPoints-1)
      ), None),
      lambda w: (w._replace(g=w.g._replace(
          holeDeep=w.g.holeDeep + DIGGING_NORMAL_DEEP,
          actionPoints=w.g.actionPoints-1)
      ), None),
      lambda w: (w, None),
      showChangedPropsAfterAll=True,
  )


def __calcDice__(rt):
  digLA = LEVEL_DIGGING_COEFF * rt.g.diggingLevel
  digI = DIG_INTELLIGENCE_COEFF * rt.g.intelligence + digLA
  digS = DIG_STRENGTH_COEFF * rt.g.strenght + digLA
  avrg = (digI + digS) / 2
  digBuff = min(avrg, max(digI, digS))

  digBuff = 0  # TEMP

  dd = (20, 1)
  dice = rollDice(dd[0])
  d = dice + digBuff
  showRollResult(
      YOU_STRING,
      '{} + {}'.format(
          dice,
          digBuff
      ),
      'd{}x{} + digBuff'.format(
          green(dd[0]),
          green(dd[1]),
      ),
      d,
      DIGGING_EVENT_FAILURE_CRIT_BOUND,
      DIGGING_EVENT_FAILURE_SIMPLE_BOUND,
      DIGGING_EVENT_SUCCESS_SIMPLE_BOUND,
  )

  return d
