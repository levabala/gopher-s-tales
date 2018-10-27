from random import randint
from scripts.visual.ConsoleColors import bcolors
from scripts.visual.Methods import showStory


def rollDice(rang=6):
  return randint(1, rang)


def showRollResult(who, values, variables, *bounds):
  strBounds = ', '.join([
      '> {}{}{}'.format(bcolors.BOLD, bound, bcolors.ENDC)
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
