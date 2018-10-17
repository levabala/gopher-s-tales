from classes.ConsoleColors import bcolors
from classes.GopherVisual import formatValueColored
from classes.Gopher import Gopher

RESPECT_A_COEFF = 1
RESPECT_B_COEFF = 1
DIG_INTELLIGENCE_COEFF = 1
DIG_STRENGTH_COEFF = 1
LEVEL_DIGGING_COEFF = 1
LEVEL_FIGHTING_COEFF = 1
LEVEL_TRADING_COEFF = 1


def getDigDeep(gopher):
  digLA = LEVEL_DIGGING_COEFF * gopher.diggingLevel
  digI = DIG_INTELLIGENCE_COEFF * gopher.intelligence + digLA
  digS = DIG_STRENGTH_COEFF * gopher.strenght + digLA
  avrg = (digI + digS) / 2
  return min(avrg, max(digI, digS))


def calcRespect(gopher):
  return RESPECT_A_COEFF * gopher.fame + RESPECT_B_COEFF * gopher.wealth


def isDied(g):
  return g.health <= 0 or g.holeDeep <= 0 or g.weight <= 0


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


def pr2rn(gopher):
  """Properties to range"""
  # I LOVE GENERATORS
  # I REAALY LOVE THEN
  return Gopher(
      *[min(max(prop, 0), 1) if type(prop) is float else prop for prop in gopher]
  )


def showActionsLeft(gopher):
  print('{}{}{} action{} left'.format(
      bcolors.HEADER,
      gopher.actionPoints,
      bcolors.ENDC,
      's' if gopher.actionPoints != 1 else '')
  )
