from random import randint
from classes.ConsoleColors import bcolors
from classes.GopherVisual import (
    formatValueChanged, formatValueColored,
    showActionsLeft, showChangedProps,
    showCharacter, CRITICAL_FAILURE, SIMPLE_FAILURE, SIMPLE_SUCCESS)
from classes.Gopher import Gopher
from classes.Constants import *
from classes.events.FloodEvent import FloodEvent
from classes.events.DownfallEvent import DownfallEvent
from classes.SmoothPrint import smoothPrint


def updateRespect(rt):
  return rt._replace(g=rt.g._replace(respect=calcRespect(rt.g)))


def calcRespect(gopher):
  return RESPECT_A_COEFF * gopher.fame + RESPECT_B_COEFF * gopher.wealth


def calcWeekTax(gopher):
  return START_WEALTH / 4 + gopher.wealth * WEEK_TAX


def isDead(gopher):
  return gopher.health <= 0 or gopher.holeDeep <= 0 or gopher.weight <= 0


def gopherStateAfterNight(gopher):
  notToPrint = 'name strenght agility intelligence charisma origin'.split(' ')
  return '\n'.join(
      [
          '{}{}{} is now: {}'.format(
              bcolors.BOLD, f, bcolors.ENDC,
              formatValueColored(getattr(gopher, f), getattr(gopher, f))
          )
          for f in gopher._fields if not f in notToPrint
      ]
  )


def pr2rn(rt):
  """Properties to range"""

  excluded = 'wealth actionPoints respect'.split(' ')

  # I LOVE GENERATORS
  # I REAALY LOVE THEM
  return rt._replace(
      g=Gopher(*[min(max(prop, 0), 1) if type(prop)
                 is float and not propName in excluded else prop for propName, prop in rt.g._asdict().items()])
  )
