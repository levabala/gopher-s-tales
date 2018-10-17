from classes.Gopher import Gopher, defaultGopher
from classes.ConsoleColors import bcolors
from classes.GopherVisual import formatValueColored
from toolz.functoolz import pipe

AFTER_SLEEP_ACTION_POINTS = 2


def runGameCycle(exitCommand='exit', gopher=defaultGopher('Jackobs')):
  print('\n\n{} wakes up in a countryside'.format(gopher.name))

  gopher = gopher._replace(actionPoints=AFTER_SLEEP_ACTION_POINTS)
  daysLived = days(gopher)
  print('\n--- FINISH ---\nyour survived for: {} days'.format(daysLived))


actions = {
    'dig': lambda g: g._replace(
        holeDeep=g.holeDeep + (1 - g.holeDeep) * 0.1,
        actionPoints=g.actionPoints - 1
    ),
    'sleep': lambda g: g._replace(
        actionPoints=AFTER_SLEEP_ACTION_POINTS,
        holeDeep=g.holeDeep - 0.2,
        health=g.health + 0.2,
        fame=g.fame - 0.1,
        weight=g.weight - 1 / 6
    ),
    'myprops': lambda g: showCharacter(g)
}


def days(gopher, day=0):
  print('\n--- Day {} ---\n'.format(day))

  # do all actions:
  # 1. perform user actions
  # 2. sleep for night
  # 3. check if is died
  gopher = pipe(gopher, controlByUser, actions['sleep'], pr2rn)
  died = isDied(gopher)

  # print after-night props
  print('\n' + gopherStateAfterNight(gopher))

  # if not died then go to the next day
  if (died):
    return day
  else:
    return days(gopher, day + 1)


def showActionsLeft(gopher):
  print('{}{}{} action{} left'.format(
      bcolors.HEADER,
      gopher.actionPoints,
      bcolors.ENDC,
      's' if gopher.actionPoints != 1 else '')
  )


def isDied(g):
  return g.health <= 0 or g.holeDeep <= 0 or g.weight <= 0


def controlByUser(gopher):
  while gopher.actionPoints > 0:
    gopher = pipe(gopher, getUserAction(), pr2rn)
    showActionsLeft(gopher)
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


def gopherStateAfterNight(gopher):
  notToPrint = 'name strenght agility intelligence charisma origin'.split(' ')
  return '\n'.join(
      [
          '{}{}{} is now: {}'.format(
              bcolors.BOLD, f, bcolors.ENDC,
              formatValueColored(getattr(gopher, f))
          )
          for f in gopher._fields if not f in notToPrint
      ]
  )


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
  print(string)
  return gopher


def pr2rn(gopher):
  """Properties to range"""
  # I LOVE GENERATORS
  # I REAALY LOVE THEN
  return Gopher(
      *[min(max(prop, 0), 1) if type(prop) is float else prop for prop in gopher]
  )
