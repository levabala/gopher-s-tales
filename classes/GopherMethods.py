from random import randint
from classes.ConsoleColors import bcolors
from classes.GopherVisual import *
from classes.Gopher import Gopher
from classes.Constants import *
from classes.Events import floodEvent, downFallEvent
from classes.Assets import d20


def performDig(rt):
  digLA = LEVEL_DIGGING_COEFF * rt.g.diggingLevel
  digI = DIG_INTELLIGENCE_COEFF * rt.g.intelligence + digLA
  digS = DIG_STRENGTH_COEFF * rt.g.strenght + digLA
  avrg = (digI + digS) / 2
  digBuff = min(avrg, max(digI, digS))

  digBuff = 0  # TEMP

  d = d20() + digBuff

  if d < DIGGING_FAILURE_CRIT_BOUND:
    printCriticalFailure()
    event = floodEvent if randint(0, 1) else downFallEvent
    return rt._replace(e=rt.e + [event], g=rt.g._replace(actionPoints=0))
  elif d < DIGGING_FAILURE_SIMPLE_BOUND:
    printFailure()
    return rt._replace(g=rt.g._replace(
        holeDeep=rt.g.holeDeep - DIGGING_NORMAL_DEEP,
        actionPoints=rt.g.actionPoints-1)
    )
  elif d < DIGGING_SUCCESS_SIMPLE_BOUND:
    printSuccess()
    return rt._replace(g=rt.g._replace(
        holeDeep=rt.g.holeDeep + DIGGING_NORMAL_DEEP,
        actionPoints=rt.g.actionPoints-1)
    )

  # should be never
  raise Exception('very strange dice')


def calcRespect(gopher):
  return RESPECT_A_COEFF * gopher.fame + RESPECT_B_COEFF * gopher.wealth


def isDied(gopher):
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


def showCharacter(gopher):
  toPrint = 'name strenght agility intelligence charisma origin'.split(' ')
  string = '\n'.join(
      [
          '{}{}{} is now: {}'.format(
              bcolors.BOLD, f, bcolors.ENDC,
              formatValueColored(getattr(gopher, f))
          )
          for f in gopher._fields if f in toPrint
      ]
  )
  print(string)
  return gopher


def pr2rn(rt):
  """Properties to range"""
  # I LOVE GENERATORS
  # I REAALY LOVE THEN
  return rt._replace(
      g=Gopher(*[min(max(prop, 0), 1) if type(prop) is float else prop for prop in rt.g])
  )


def showActionsLeft(gopher):
  print('{}{}{} action{} left'.format(
      bcolors.HEADER,
      gopher.actionPoints,
      bcolors.ENDC,
      's' if gopher.actionPoints != 1 else '')
  )


def showChangedProps(gopher1, gopher2, propsExcept=[]):
  for propName in [field for field in gopher1._fields if not field in propsExcept]:
    val1 = getattr(gopher1, propName)
    val2 = getattr(gopher2, propName)
    if val1 != val2:
      print(formatValueChanged(
          propName,
          val2,
          val2 - val1 if type(val1) == float or type(val1) == int else None
      ))
