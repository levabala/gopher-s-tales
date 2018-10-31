import math
from scripts.WorldMethods import getRegion
from scripts.visual.Converter import COEFFS, POSTFIXES
from scripts.visual.ConsoleColors import bcolors
from scripts.visual.SmoothPrint import smoothPrint
from scripts.Constants import SMALL_DELAY, MEDIUM_DELAY, BIG_DELAY

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


def showChangedProps(gopher1, gopher2, propsExcept=[], prefix='', postPrint=True):
  arr = [field for field in gopher1._fields if not field in propsExcept]
  printed = 0
  for propName in arr:
    val1 = getattr(gopher1, propName)
    val2 = getattr(gopher2, propName)
    if val1 != val2:
      val1Trfrm = round(val1 * COEFFS[propName], ROUND_DIGITS)
      val2Trfrm = round(val2 * COEFFS[propName], ROUND_DIGITS)
      smoothPrint(formatValueChanged(
          prefix + propName,
          val2Trfrm,
          val2,
          val2Trfrm - val1Trfrm if type(val1) == float or type(val1) == int else None
      ), SMALL_DELAY)
      printed += 1

  if not postPrint:
    return

  if printed:
    print()
  else:
    smoothPrint('>> nothing changed\n')


def getCurrentMapCollection(w):
  if w.currentAreaPointer is None:
    return (w.regions, w.currentRegionPointer)
  else:
    region = getRegion(w, w.currentRegionPointer)
    return (region['areas'], w.currentAreaPointer)


def showMap(w):
  y = 0
  collection, pointer = getCurrentMapCollection(w)
  for line in collection:
    elements = [el['area name'].center(8) for el in line]

    string = ''
    x = 0
    for el in elements:
      if (
          y == pointer.y and
          x == pointer.x
      ):
        string += '{}{}{}'.format(bcolors.BOLD, el, bcolors.ENDC)
      else:
        string += el
      string += ' '
      x += 1

    smoothPrint(string)
    smoothPrint()

    y += 1

  print()

  return w


def showInventory(w):
  counter = 0
  smoothPrint('Your inventory:')
  for elem in sorted([el['name'] for el in w.g.inventory]):
    counter += 1
    smoothPrint('  {}: {}'.format(counter, elem))

  return w


def showThings(w):
  counter = 0
  smoothPrint('Your things:')
  for elem in sorted(w.g.equipement + w.g.inventory, key=lambda el: el['name']):
    counter += 1
    name = elem['name']
    if elem['equiped']:
      smoothPrint('  {}: {}{}{}'.format(counter, bcolors.BOLD, name, bcolors.ENDC))
    else:
      smoothPrint('  {}: {}'.format(counter, name))

  return w
