import math
from scripts.WorldMethods import getCurrentArea, getCurrentRegion
from scripts.visual.Converter import COEFFS, POSTFIXES
from scripts.visual.ConsoleColors import bcolors, green
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

  for line in lines:
    line = line.lstrip()
    smoothPrint('{}{}'.format('' if len(line) == 0 else '| ', line))
  print()


def showLifeProps(w):
  toPrint = '''
    health weight fame holeDeep wealth respect
  '''.replace('\n', '').strip().split(' ')
  for f in [f for f in w.g._fields if f in toPrint]:
    val = getattr(w.g, f)
    smoothPrint('{}{}{} is now: {}'.format(
        bcolors.BOLD, f, bcolors.ENDC,
        formatValueColored(val * COEFFS[f], val)), SMALL_DELAY)
  print()
  return w


def showSpecialProps(w, toPrint=[]):
  for f in [f for f in w.g._fields if f in toPrint]:
    val = getattr(w.g, f)
    smoothPrint('{}{}{} is now: {}'.format(
        bcolors.BOLD, f, bcolors.ENDC,
        formatValueColored(val * COEFFS[f], val)), SMALL_DELAY)
  print()
  return w


def showProps(w):
  toExcept = '''
    name quickSlot
    origin equipement inventory alive
  '''.replace('\n', '').strip().split(' ')
  for f in [f for f in w.g._fields if not f in toExcept]:
    val = getattr(w.g, f)
    smoothPrint('{}{}{} is now: {}'.format(
        bcolors.BOLD, f, bcolors.ENDC,
        formatValueColored(val * COEFFS[f], val)), SMALL_DELAY)
  print()
  return w


def showCharacter(w):
  toPrint = 'name strenght agility intelligence charisma origin'.split(' ')
  for f in [f for f in w.g._fields if f in toPrint]:
    val = getattr(w.g, f)
    smoothPrint('{}{}{} is now: {}'.format(
        bcolors.BOLD, f, bcolors.ENDC,
        formatValueColored(
            val * COEFFS[f] if type(val) == int or type(val) == float else val, val
        )
    ), SMALL_DELAY)
  print()
  return w


def showActionsLeft(gopher):
  smoothPrint('{}{}{} action{} left'.format(
      bcolors.HEADER,
      gopher.actionPoints,
      bcolors.ENDC,
      's' if gopher.actionPoints != 1 else ''), SMALL_DELAY)
  print()


def showChangedProps(gopher1, gopher2, propsExcept=[], prefix='', postPrint=True, printIfNothing=True):
  propsExcept += [
      'equipement',
      'inventory',
      'quickSlot',
      'alive',
      'origin',
      'name',
  ]  # default except

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
  elif printIfNothing:
    smoothPrint('>> nothing changed\n')


def showMap(w):
  y = 0
  pointer = w.locationPath[-1]

  collection = getCurrentRegion(w)['areas']
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


def showEquipment(w):
  counter = 0
  smoothPrint('Your equipement:')
  for elem in sorted(w.g.equipement, key=lambda el: el['name']):
    counter += 1
    smoothPrint('  {}: {}{}{}'.format(counter, bcolors.BOLD, elem['name'], bcolors.ENDC))

  return w


def showInventory(w, highlightEquiped=False):
  counter = 0
  smoothPrint('Your inventory (not equipement):')

  inventory = sorted(w.g.inventory, key=lambda el: el['name'])
  equipement = w.g.equipement
  for elem in inventory:
    counter += 1
    equipedSameType = next(
        (el for el in equipement if el['type'] == elem['type']),
        False)
    if equipedSameType and highlightEquiped:
      smoothPrint('  {}{}:{} {}'.format(bcolors.FAIL, counter, bcolors.ENDC, elem['name']))
    else:
      smoothPrint('  {}: {}'.format(counter, elem['name']))

  return w._replace(g=w.g._replace(inventory=inventory))


def showThings(w):
  counter = 0
  smoothPrint('Your things:')

  things = sorted(w.g.equipement + w.g.inventory, key=lambda el: el['name'])
  for elem in things:
    counter += 1
    name = elem['name']
    if elem['equiped']:
      smoothPrint('  {}: {}{}{}'.format(counter, bcolors.BOLD, name, bcolors.ENDC))
    else:
      smoothPrint('  {}: {}'.format(counter, name))

  inventory = sorted(w.g.inventory, key=lambda el: el['name'])
  equipement = sorted(w.g.equipement, key=lambda el: el['name'])

  return w._replace(g=w.g._replace(inventory=inventory, equipement=equipement))


def showThingProps(thing):
  m = {
      'type': lambda p: 'type: {}{}{}'.format(bcolors.OKGREEN, p, bcolors.ENDC),
      'weight': lambda p: 'weight: {}'.format(green(p * COEFFS['strength'])),
      'dice': lambda p: '(edges, count): d{}{}{}x{}{}{}'.format(
          bcolors.OKGREEN, p[0], bcolors.ENDC,
          bcolors.OKGREEN, p[1], bcolors.ENDC,
      ),
      'sm': lambda p: 'smash: {}{}{}p'.format(bcolors.OKGREEN, p, bcolors.ENDC),
      'sl': lambda p: 'slice: {}{}{}p'.format(bcolors.OKGREEN, p, bcolors.ENDC),
      'pr': lambda p: 'pierce: {}{}{}p'.format(bcolors.OKGREEN, p, bcolors.ENDC),
      'fr': lambda p: 'fire: {}{}{}p'.format(bcolors.OKGREEN, p, bcolors.ENDC),
      'ac': lambda p: 'acid: {}{}{}p'.format(bcolors.OKGREEN, p, bcolors.ENDC),
  }

  smoothPrint('Thing "{}{}{}"'.format(bcolors.OKGREEN, thing['name'], bcolors.ENDC))

  mKeys = m.keys()
  for k in sorted(thing.keys()):
    if k in mKeys:
      smoothPrint('  - ' + m[k](thing[k]))
