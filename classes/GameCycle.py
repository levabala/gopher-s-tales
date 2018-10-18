from toolz.functoolz import pipe
from collections import namedtuple
from copy import deepcopy
from classes.Gopher import Gopher, defaultGopher
from classes.GopherMethods import *
from classes.Constants import SMALL_DELAY, MEDIUM_DELAY, BIG_DELAY
from classes.SmoothPrint import smoothPrint
from classes.GopherVisual import showStory

RT = namedtuple('ReturnTuple', 'g e')  # gopher events


def runGameCycle(exitCommand='exit', gopher=defaultGopher('Jackobs')):
  showStory('\n\n{} wakes up in a countryside'.format(gopher.name), raw=True)

  gopher = gopher._replace(actionPoints=AFTER_SLEEP_ACTION_POINTS)
  daysLived = days(RT(g=gopher, e=[]))
  smoothPrint('\n--- FINISH ---\nyour survived for: {} days'.format(daysLived))


actions = {
    'dig': lambda rt: performDig(rt),
    'sleep': lambda rt: RT(
        g=rt.g._replace(
            actionPoints=AFTER_SLEEP_ACTION_POINTS,
            holeDeep=rt.g.holeDeep - 0.02,
            health=rt.g.health + 0.1,
            fame=rt.g.fame - 0.01,
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
  smoothPrint('\n--- Day {} ---\n'.format(day), BIG_DELAY)
  gopherBefore = deepcopy(rt.g)

  # do all actions:
  # 0. we use ReturnTuple (see above)
  # 1. perform user actions
  # 2. sleep for night
  # 3. check if is died
  rt = controlByUser(rt)

  gopherAfterDay = rt.g
  rt = actions['sleep'](rt)
  smoothPrint('{}AFTER DAY CHANGES{}'.format(bcolors.BOLD, bcolors.ENDC))
  showChangedProps(gopherBefore, gopherAfterDay, ['actionPoints'])

  rt = pr2rn(rt)

  died = isDied(rt.g)

  # smoothPrint after-night props
  gopherAfterDayAndNight = rt.g
  smoothPrint('\n{}AFTER DAY&NIGHT CHANGES{}'.format(bcolors.BOLD, bcolors.ENDC))

  showChangedProps(gopherBefore, gopherAfterDayAndNight, ['actionPoints'])
  # smoothPrint('\n' + gopherStateAfterNight(rt.g))

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
    gopherBeforeEvent = deepcopy(rt.g)
    rt._replace(g=event(rt.g))
    gopherAfterEvent = rt.g
    showChangedProps(gopherBeforeEvent, gopherAfterEvent, ['actionPoints'])

  # display changes
  gopherAfter = rt.g
  showChangedProps(gopherBefore, gopherAfter, ['actionPoints'])

  return rt


def getUserAction():
  # request action
  actionName = input('Enter action to do: ')
  print()

  # check if action exists
  if not actionName in actions:
    print('no such action!\n')
    return getUserAction()
  else:
    return actions[actionName]
