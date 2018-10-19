from random import randint
from classes.ConsoleColors import bcolors
from classes.GopherVisual import (
    formatValueChanged, formatValueColored,
    showActionsLeft, showChangedProps,
    showCharacter, CRITICAL_FAILURE, SIMPLE_FAILURE, SIMPLE_SUCCESS)
from classes.Gopher import Gopher
from classes.Constants import *
from classes.Events import floodEvent, downfallEvent
from classes.Assets import d20
from classes.SmoothPrint import smoothPrint


def performDig(rt):
  digLA = LEVEL_DIGGING_COEFF * rt.g.diggingLevel
  digI = DIG_INTELLIGENCE_COEFF * rt.g.intelligence + digLA
  digS = DIG_STRENGTH_COEFF * rt.g.strenght + digLA
  avrg = (digI + digS) / 2
  digBuff = min(avrg, max(digI, digS))

  digBuff = 0  # TEMP

  d = d20() + digBuff

  if d < DIGGING_FAILURE_CRIT_BOUND:
    smoothPrint(CRITICAL_FAILURE)
    event = floodEvent if randint(0, 1) else downfallEvent
    return rt._replace(e=rt.e + [event], g=rt.g._replace(actionPoints=0))
  elif d < DIGGING_FAILURE_SIMPLE_BOUND:
    smoothPrint(SIMPLE_FAILURE)
    return rt._replace(g=rt.g._replace(
        actionPoints=rt.g.actionPoints-1)
    )
  elif d < DIGGING_SUCCESS_SIMPLE_BOUND:
    smoothPrint(SIMPLE_SUCCESS)
    return rt._replace(g=rt.g._replace(
        holeDeep=rt.g.holeDeep + DIGGING_NORMAL_DEEP,
        actionPoints=rt.g.actionPoints-1)
    )

  # should be never
  raise Exception('very strange dice')


def calcRespect(gopher):
  return RESPECT_A_COEFF * gopher.fame + RESPECT_B_COEFF * gopher.wealth


def isDead(gopher):
  return gopher.health <= 0 or gopher.holeDeep <= 0 or gopher.weight <= 0


def gopherStateAfterNight(gopher):
  notToPrint = 'name strenght agility intelligence charisma origin'.split(' ')
  return '\n'.join(
      [
          '{}{}{} is now: {}'.format(
              bcolors.BOLD, f, bcolors.ENDC,
              formatValueColored(getattr(gopher, f))
          )
          for f in gopher._fields if not f in notToPrint
      ]
  )


def pr2rn(rt):
  """Properties to range"""
  # I LOVE GENERATORS
  # I REAALY LOVE THEM
  return rt._replace(
      g=Gopher(*[min(max(prop, 0), 1) if type(prop) is float else prop for prop in rt.g])
  )
