from random import randint
from scripts.visual.ConsoleColors import bcolors
from scripts.visual.Methods import showStory


def rollDice(rang=6, dices=1):
  return sum([randint(1, rang) for i in range(dices)])


def showRollResult(who, values, variables, *bounds):
  strBounds = ', '.join([
      '> {}{}{}'.format(bcolors.BOLD, round(bound, 1), bcolors.ENDC)
      for bound in bounds
  ])
  string = '''
    {} rolled: {}{} = {}{},
    calced by: {}{}{},
    for success: {}
  '''.format(
      who,
      bcolors.BOLD,
      ' + '.join(str(round(v, 2)) for v in values),
      str(round(sum(values), 2)),
      bcolors.ENDC,
      bcolors.BOLD,
      ' + '.join(variables),
      bcolors.ENDC,
      strBounds,
  )
  showStory(string)
