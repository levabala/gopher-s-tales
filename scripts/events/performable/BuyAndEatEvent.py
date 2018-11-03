from scripts.EventPipe import EventPipe
from scripts.events.MoveEvent import MoveEvent
from scripts.events.Event import EventTrivialFunc
from scripts.WorldMethods import isPointerValid
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showMap, showStory, showSpecialProps
from scripts.visual import ConsoleColors
from scripts.GopherMethods import calcDiscountCoeff
from texts.events import EmptyTexts
from scripts.structures.Point import Point
from scripts.visual.Converter import COEFFS

from scripts.food.Bread import Bread
from scripts.food.Cake import Cake
from scripts.food.MagicApple import MagicApple

food = [
    Bread,
    Cake,
    MagicApple,
]


def BuyAndEatEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process,
      showChangedPropsAfterAll=True,
  )


def _process(w):
  def nextPlease(w):
    showStory('Invalid index', raw=True)
    print()

    return (w, BuyAndEatEvent)

  showSpecialProps(w, ['wealth', 'weight', 'fame'])

  smoothPrint('Available food:')
  index = 0
  coeff = calcDiscountCoeff(w.g)
  for f in food:
    discound = f.cost * coeff
    string = '  {}. {} (cost: {}({}), weight: {}, discound: {})'.format(
        index + 1,
        f.name,
        ConsoleColors.green(
            round(f.cost * COEFFS['wealth'] - discound * COEFFS['wealth'], 1)),
        ConsoleColors.green(
            round(f.cost * COEFFS['wealth'], 1)),
        ConsoleColors.green(f.value * COEFFS['weight']),
        ConsoleColors.green(round(discound * COEFFS['wealth'], 1)),
    )
    smoothPrint(string)

    index += 1

  mess = 'Enter item to buy&eat index: '
  print()
  num = input(mess)
  print()

  if not num.isdigit():
    if num == 'abort':
      return (w, None)
    return nextPlease(w)

  num = int(num) - 1

  if (
      (num < 0) or
      (num > len(food) - 1)
  ):
    return nextPlease(w)

  cost = food[num].cost * (1 - coeff)
  if cost > w.g.wealth:
    showStory('Too expensive for you', True)
    return nextPlease(w)

  # buy&eat
  return (w._replace(g=w.g._replace(
      wealth=w.g.wealth - cost,
      weight=w.g.weight + food[num].value
  )), None)
