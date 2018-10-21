from classes.Event import __EventTrivialFunc__
from texts.events import FightTexts
from classes.Constants import *
from classes.GopherMethods import calcRespect
from classes.GopherVisual import showStory
from classes.descriptions.MinDescription import getMinDescription
from classes.descriptions.MediumDescription import getMediumDescription
from classes.descriptions.FullDescription import getFullDescription


def FightEvent(rt):
  return __EventTrivialFunc__(
      rt,
      FightTexts,
      do,
  )


def do(rt):
  # get description
  enemy = rt.w.currentEnemy
  gopher = rt.g

  description = None
  if rt.g.intelligence < MIN_ENEMY_DESCRIPTION_INTELLIGENCE_BOUND:
    description = getMinDescription(enemy)
  elif rt.g.intelligence < MEDIUM_ENEMY_DESCRIPTION_INTELLIGENCE_BOUND:
    description = getMediumDescription(enemy)
  elif rt.g.intelligence < FULL_ENEMY_DESCRIPTION_INTELLIGENCE_BOUND:
    description = getFullDescription(enemy)
  string = '\n'.join(['{}: {}'.format(name, getattr(description, name))
                      for name in description._fields])

  showStory(string)

  # actions loop
  global oneGone
  oneGone = False

  def retreat(gopher, enemy):
    global oneGone
    oneGone = True
    return (gopher, enemy)

  while enemy.health > 0 and rt.g.health > 0 and not oneGone:
    # choose action
    actions = {
        'hit': lambda gopher, enemy: (gopher, enemy),
        'heavy hit': lambda gopher, enemy: (gopher, enemy),
        'prepare': lambda gopher, enemy: (gopher, enemy),
        'change weapon': lambda gopher, enemy: (gopher, enemy),  # changeWeaponEvent
        'use thing': lambda gopher, enemy: (gopher, enemy),  # useThingEvent ?
        'retreat': lambda gopher, enemy: retreat(gopher, enemy)
    }

    # TODO: realize everything as Event ¯\_(ツ)_/¯

    actionName = ''
    while not actionName in actions:
      actionName = input('Enter action name: ')

    action = actions[actionName]

    # perform you action
    gopher, enemy = action(gopher, enemy)

    # enemy action
    # gopher, enemy = enemyAction(gopher, enemy)

  return rt
