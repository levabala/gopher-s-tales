from classes.ConsoleColors import bcolors
from classes.SmoothPrint import smoothPrint
from classes.Constants import SMALL_DELAY, MEDIUM_DELAY, BIG_DELAY

ROUND_DIGITS = 2


def formatValueColored(value):
  start = ''
  if not type(value) is float:
    start = bcolors.OKBLUE
  else:
    value = round(value, ROUND_DIGITS)
    if value <= 0.2:
      start = bcolors.FAIL
    elif value < 0.5:
      start = bcolors.WARNING
    elif value < 0.7:
      start = bcolors.OKBLUE
    else:
      start = bcolors.OKGREEN

  return "{}{}{}".format(start, value, bcolors.ENDC)


def formatValueChanged(name, value, delta):
  if delta != None:
    return '>> {} changed to {} ({}{})'.format(
        name,
        formatValueColored(value),
        '+' if delta >= 0 else '',
        round(delta, ROUND_DIGITS)
    )
  else:
    return '>> {} changed to {}'.format(
        name,
        formatValueColored(value),
    )


CRITICAL_SUCCESS = '{}CRITICAL SUCCESS{}'.format(bcolors.HEADER, bcolors.ENDC)
SIMPLE_SUCCESS = '{}SUCCESS{}'.format(bcolors.OKGREEN, bcolors.ENDC)
SIMPLE_FAILURE = '{}FAILURE{}'.format(bcolors.WARNING, bcolors.ENDC)
CRITICAL_FAILURE = '{}CRITICAL FAILURE{}'.format(bcolors.FAIL, bcolors.ENDC)


def showStory(text):
  lines = text.split('\n')
  for line in lines:
    smoothPrint('{}{}'.format('' if len(line.lstrip()) == 0 else '| ', line))


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
  smoothPrint(string, SMALL_DELAY)
  return gopher


def showActionsLeft(gopher):
  smoothPrint('{}{}{} action{} left'.format(
      bcolors.HEADER,
      gopher.actionPoints,
      bcolors.ENDC,
      's' if gopher.actionPoints != 1 else ''), SMALL_DELAY)


def showChangedProps(gopher1, gopher2, propsExcept=[]):
  for propName in [field for field in gopher1._fields if not field in propsExcept]:
    val1 = getattr(gopher1, propName)
    val2 = getattr(gopher2, propName)
    if val1 != val2:
      smoothPrint(formatValueChanged(
          propName,
          val2,
          val2 - val1 if type(val1) == float or type(val1) == int else None
      ), SMALL_DELAY)
