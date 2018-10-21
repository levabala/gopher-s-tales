from random import randint
from classes.ConsoleColors import bcolors
from classes.GopherVisual import showStory


def rollDice(rang=6):
  return randint(1, rang)


def showRollResult(values, variables, successBound):
  string = '''
    you rolled: {}{} = {}{},
    cacled by: {}{}{},
    for success: > {}{}{}
  '''.format(
      bcolors.BOLD,
      ' + '.join(str(round(v, 2)) for v in values),
      str(round(sum(values), 2)),
      bcolors.ENDC,
      bcolors.BOLD,
      ' + '.join(variables),
      bcolors.ENDC,
      bcolors.BOLD,
      str(successBound),
      bcolors.ENDC,
  )
  showStory(string)
