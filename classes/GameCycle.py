from toolz.functoolz import pipe
from collections import namedtuple
from classes.Gopher import Gopher, defaultGopher
from classes.GopherMethods import *

ReturnTuple = namedtuple('ReturnTuple', 'g e')  # gopher events


def runGameCycle(exitCommand='exit', gopher=defaultGopher('Jackobs')):
  print('\n\n{} wakes up in a countryside'.format(gopher.name))

  gopher = gopher._replace(actionPoints=AFTER_SLEEP_ACTION_POINTS)
  daysLived = days(gopher)
  print('\n--- FINISH ---\nyour survived for: {} days'.format(daysLived))


actions = {
    'dig': lambda rt: ReturnTuple(
        g=rt.g._replace(
            holeDeep=rt.g.holeDeep + getDigDeep(rt.g),
            actionPoints=rt.g.actionPoints - 1
        ),
        e=rt.e),
    'sleep': lambda rt:
    ReturnTuple(
        g=rt.g._replace(
            actionPoints=AFTER_SLEEP_ACTION_POINTS,
            holeDeep=rt.g.holeDeep - 0.2,
            health=rt.g.health + 0.2,
            fame=rt.g.fame - 0.1,
            weight=rt.g.weight - 1 / 6,
            respect=calcRespect(rt.g)
        ),
        e=rt.e),
    'myprops': lambda g: showCharacter(g),
    # not implemented
    'eat': lambda g: g,
    'fight': lambda g: g,
    'trade': lambda g: g,
}


def days(gopher, day=0):
  print('\n--- Day {} ---\n'.format(day))

  # do all actions:
  # 1. perform user actions
  # 2. sleep for night
  # 3. check if is died
  gopher = pipe(ReturnTuple(g=gopher, e=[]), controlByUser, actions['sleep'], pr2rn)
  died = isDied(gopher)

  # TODO: implement RetureTuple

  # print after-night props
  print('\n' + gopherStateAfterNight(gopher))

  # if not died then go to the next day
  if (died):
    return day
  else:
    return days(gopher, day + 1)


def controlByUser(gopher):
  while gopher.actionPoints > 0:
    gopher = performAction(gopher, getUserAction())
    showActionsLeft(gopher)
  return gopher


def performAction(gopher, action):
  gopher = pipe(gopher, action, pr2rn)
  return gopher


def getUserAction():
  # request action
  actionName = input('Enter action to do: ')

  # check if action exists
  if not actionName in actions:
    print('no such action!\n')
    return getUserAction()
  else:
    return actions[actionName]
