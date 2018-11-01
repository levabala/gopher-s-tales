from random import randint
from scripts.visual.ConsoleColors import bcolors, green, bold
from scripts.visual.Methods import showStory


def rollDice(rang=6, dices=1):
  return sum([randint(1, rang) for i in range(dices)])


def showRollResult(who, rollString, exprString, sum, *bounds):
  strBounds = ', '.join([
      '> {}'.format(green(round(bound, 1)))
      for bound in bounds
  ])
  string = '''
    {} rolled: {} = {},
    calced by: {},    
    for success: {}
  '''.format(
      who,
      rollString,
      green(round(sum, 1)),
      bold(exprString),
      strBounds,
  )
  showStory(string)


def showRollResultAttack(who, coeffString, rollString, exprString, sum, *bounds):
  strBounds = ', '.join([
      '> {}'.format(green(round(bound, 1)))
      for bound in bounds
  ])
  string = '''
    {} rolled: {} = {},
    calced by: {},
    attack coeff: {},
    for success: {}
  '''.format(
      who,
      rollString,
      green(round(sum, 1)),
      bold(exprString),
      coeffString,
      strBounds,
  )
  showStory(string)
