import math
from classes.Converter import COEFFS, POSTFIXES
from classes.ConsoleColors import bcolors
from classes.SmoothPrint import smoothPrint
from classes.Constants import SMALL_DELAY, MEDIUM_DELAY, BIG_DELAY

ROUND_DIGITS = 2


def formatValueColored(value, valueRaw):
  start = ''
  if not type(valueRaw) is float:
    start = bcolors.OKBLUE
  else:
    value = round(value, ROUND_DIGITS)
    if valueRaw <= 0.2:
      start = bcolors.FAIL
    elif valueRaw < 0.5:
      start = bcolors.WARNING
    elif valueRaw < 0.7:
      start = bcolors.OKBLUE
    else:
      start = bcolors.OKGREEN

  return "{}{}{}".format(start, value, bcolors.ENDC)


def formatValueChanged(name, value, valueRaw, delta):
  if delta != None:
    return '>> {} changed to {}{} ({}{}{})'.format(
        name,
        formatValueColored(value, valueRaw),
        '',  # POSTFIXES[name],
        '+' if delta >= 0 else '',
        round(delta, ROUND_DIGITS),
        '',  # POSTFIXES[name],
    )
  else:
    return '>> {} changed to {}'.format(
        name,
        formatValueColored(value, valueRaw),
    )


CRITICAL_SUCCESS = '{}CRITICAL SUCCESS{}'.format(bcolors.HEADER, bcolors.ENDC)
SIMPLE_SUCCESS = '{}SUCCESS{}'.format(bcolors.OKGREEN, bcolors.ENDC)
SIMPLE_FAILURE = '{}FAILURE{}'.format(bcolors.WARNING, bcolors.ENDC)
CRITICAL_FAILURE = '{}CRITICAL FAILURE{}'.format(bcolors.FAIL, bcolors.ENDC)


def showStory(text, raw=False):
  lines = text.split('\n')
  if not raw:
    lines.pop(0)
    del lines[-1]

  if not lines:
    return

  print()

  if not lines:
    return

  for line in lines:
    line = line.lstrip()
    smoothPrint('{}{}'.format('' if len(line) == 0 else '| ', line))
  print()


def showCharacter(rt):
  toPrint = 'name strenght agility intelligence charisma origin'.split(' ')
  for f in [f for f in rt.g._fields if f in toPrint]:
    val = getattr(rt.g, f)
    smoothPrint('{}{}{} is now: {}'.format(
        bcolors.BOLD, f, bcolors.ENDC,
        formatValueColored(val, val)), SMALL_DELAY)
  print()
  return rt


def showActionsLeft(gopher):
  smoothPrint('{}{}{} action{} left'.format(
      bcolors.HEADER,
      gopher.actionPoints,
      bcolors.ENDC,
      's' if gopher.actionPoints != 1 else ''), SMALL_DELAY)
  print()


def showChangedProps(gopher1, gopher2, propsExcept=[]):
  arr = [field for field in gopher1._fields if not field in propsExcept]
  printed = 0
  for propName in arr:
    val1 = getattr(gopher1, propName)
    val2 = getattr(gopher2, propName)
    if val1 != val2:
      val1Trfrm = round(val1 * COEFFS[propName], ROUND_DIGITS)
      val2Trfrm = round(val2 * COEFFS[propName], ROUND_DIGITS)
      smoothPrint(formatValueChanged(
          propName,
          val2Trfrm,
          val2,
          val2Trfrm - val1Trfrm if type(val1) == float or type(val1) == int else None
      ), SMALL_DELAY)
      printed += 1

  if printed:
    print()
  else:
    smoothPrint('>> nothing changed\n')
