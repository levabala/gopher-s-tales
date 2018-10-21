from random import randint
from classes.Event import __EventFunc__
from classes.Assets import rollDice, showRollResult
from texts.events import DiggingTexts
from classes.Constants import *
from classes.GopherVisual import smoothPrint
from classes.events.FloodEvent import FloodEvent
from classes.events.DownfallEvent import DownfallEvent


def DigEvent(rt):
  return __EventFunc__(
      rt,
      DiggingTexts,
      __calcDice__,
      DIGGING_EVENT_FAILURE_CRIT_BOUND,
      DIGGING_EVENT_FAILURE_SIMPLE_BOUND,
      DIGGING_EVENT_SUCCESS_SIMPLE_BOUND,
      DIGGING_EVENT_SUCCESS_SIMPLE_BOUND,
      lambda rt: rt._replace(
          e=rt.e + [FloodEvent if randint(0, 1) else DownfallEvent],
          g=rt.g._replace(actionPoints=0)
      ),
      lambda rt: rt._replace(g=rt.g._replace(
          actionPoints=rt.g.actionPoints-1)
      ),
      lambda rt: rt._replace(g=rt.g._replace(
          holeDeep=rt.g.holeDeep + DIGGING_NORMAL_DEEP,
          actionPoints=rt.g.actionPoints-1)
      ),
      lambda rt: rt,
  )


def __calcDice__(rt):
  digLA = LEVEL_DIGGING_COEFF * rt.g.diggingLevel
  digI = DIG_INTELLIGENCE_COEFF * rt.g.intelligence + digLA
  digS = DIG_STRENGTH_COEFF * rt.g.strenght + digLA
  avrg = (digI + digS) / 2
  digBuff = min(avrg, max(digI, digS))

  digBuff = 0  # TEMP

  dice = rollDice(20)
  d = dice + digBuff
  showRollResult([dice, digBuff], ['d20', 'digBuff'], DIGGING_EVENT_SUCCESS_SIMPLE_BOUND)

  return d
