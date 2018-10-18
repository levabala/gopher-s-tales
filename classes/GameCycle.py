from toolz.functoolz import pipe
from collections import namedtuple
from copy import deepcopy
from classes.Gopher import Gopher, defaultGopher
from classes.GopherMethods import *

RT = namedtuple('ReturnTuple', 'g e')  # gopher events


def runGameCycle(exitCommand='exit', gopher=defaultGopher('Jackobs')):
  print('\n\n{} wakes up in a countryside'.format(gopher.name))

  gopher = gopher._replace(actionPoints=AFTER_SLEEP_ACTION_POINTS)
  daysLived = days(RT(g=gopher, e=[]))
  print('\n--- FINISH ---\nyour survived for: {} days'.format(daysLived))


actions = {
    'dig': lambda rt: performDig(rt),
    'sleep': lambda rt: RT(
        g=rt.g._replace(
            actionPoints=AFTER_SLEEP_ACTION_POINTS,
            holeDeep=rt.g.holeDeep - 0.2,
            health=rt.g.health + 0.2,
            fame=rt.g.fame - 0.1,
            # weight=rt.g.weight - 1 / 6,
            respect=calcRespect(rt.g)
        ),
        e=rt.e),
    'myprops': lambda rt: showCharacter(rt),
    # not implemented
    'eat': lambda rt: rt,
    'fight': lambda rt: rt,
    'trade': lambda rt: rt,
}


def days(rt, day=0):
  print('\n--- Day {} ---\n'.format(day))
  gopherBefore = deepcopy(rt.g)

  # do all actions:
  # 0. we use ReturnTuple (see above)
  # 1. perform user actions
  # 2. sleep for night
  # 3. check if is died
  rt = pipe(rt, controlByUser, actions['sleep'], pr2rn)
  died = isDied(rt.g)

  # print after-night props
  gopherAfter = rt.g
  print('\n{}AFTER DAY CHANGES{}'.format(bcolors.BOLD, bcolors.ENDC))
  showChangedProps(gopherBefore, gopherAfter)
  # print('\n' + gopherStateAfterNight(rt.g))

  # if not died then go to the next day
  if (died):
    return day
  else:
    return days(rt, day + 1)


def controlByUser(rt):
  showActionsLeft(rt.g)
  while rt.g.actionPoints > 0:
    rt = performAction(rt, getUserAction())
    showActionsLeft(rt.g)
  return rt


def performAction(rt, action):
  gopherBefore = deepcopy(rt.g)
  rt = pipe(rt, action, pr2rn)

  while rt.e:
    # take&remove first event
    event = rt.e.pop(0)

    # perform event
    rt._replace(g=event(rt.g))

  # display changes
  gopherAfter = rt.g
  showChangedProps(gopherBefore, gopherAfter, ['actionPoints'])

  print()

  return rt


def getUserAction():
  # request action
  actionName = input('Enter action to do: ')

  # check if action exists
  if not actionName in actions:
    print('no such action!\n')
    return getUserAction()
  else:
    return actions[actionName]
