from toolz.functoolz import pipe
from collections import namedtuple
from copy import deepcopy
from classes.Gopher import Gopher, defaultGopher
from classes.World import World, defaultWorld
from classes.GopherMethods import *
from classes.Constants import SMALL_DELAY, MEDIUM_DELAY, BIG_DELAY
from classes.SmoothPrint import smoothPrint
from classes.GopherVisual import showStory

# importing user-performable events
from classes.events.performable.DigEvent import DigEvent
from classes.events.performable.SleepEvent import SleepEvent
from classes.events.performable.EnterMarketEvent import EnterMarketEvent

# importing user-unperformable events
from classes.events.StartDayEvent import StartDayEvent
from classes.events.EndDayEvent import EndDayEvent

RT = namedtuple('ReturnTuple', 'g e w')  # gopher, events, world


def runGameCycle(exitCommand='exit', gopher=defaultGopher('Jackobs'), world=defaultWorld()):
  showStory('\n\n{} wakes up in a countryside'.format(gopher.name), raw=True)

  gopher = gopher._replace(actionPoints=AFTER_SLEEP_ACTION_POINTS)
  daysLived = days(RT(g=gopher, e=[], w=world))
  smoothPrint('\n--- FINISH ---\nyour survived for: {} days'.format(daysLived))


actions = {
    'dig': lambda rt: DigEvent(rt),
    'trade': lambda rt: EnterMarketEvent(rt),
    'sleep': lambda rt: SleepEvent(rt),
    'myprops': lambda rt: showCharacter(rt),

    # not implemented
    'eat': lambda rt: rt,
    'fight': lambda rt: rt,
}


def days(rt, day=0):
  # do all actions:
  # 0. we use ReturnTuple (see above)
  # 1. perform user actions
  # 2. sleep for night
  # 3. check if is died

  rt = pipe(rt, StartDayEvent, controlByUser, EndDayEvent, pr2rn)

  # check if died
  died = isDead(rt.g)

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
    rt._replace(g=event(rt))
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
