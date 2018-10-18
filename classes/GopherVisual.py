from classes.ConsoleColors import bcolors

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


def printCriticalSuccess():
  print('{}CRITICAL SUCCESS{}'.format(bcolors.HEADER, bcolors.ENDC))


def printSuccess():
  print('{}SUCCESS{}'.format(bcolors.OKGREEN, bcolors.ENDC))


def printFailure():
  print('{}FAILURE{}'.format(bcolors.WARNING, bcolors.ENDC))


def printCriticalFailure():
  print('{}CRITICAL FAILURE{}'.format(bcolors.FAIL, bcolors.ENDC))
