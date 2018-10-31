from copy import deepcopy
from scripts.EventPipe import EventPipe
from scripts.WorldMethods import getArea
from scripts.events.Event import EventTrivialFunc
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showStory, showChangedProps, formatValueColored
from scripts.EventPipe import EventPipe
from scripts.Assets import rollDice, showRollResult
from scripts.visual.Converter import COEFFS
from texts.events import EmptyTexts
from scripts.Constants import (
    LIGHT_DAMAGE_COEFF,
    FULL_DAMAGE_COEFF,
    CRIT_DAMAGE_COEFF,
    YOU_STRING,
)

from scripts.events.RecognizeMonsterEvent import RecognizeMonsterEvent
from scripts.events.fightActions.SimpleAttackEvent import SimpleAttackEvent


def FightEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  w = EventPipe(w, RecognizeMonsterEvent)

  w = w._replace(enemyState=w.enemyType.init())

  gopherBefore = None
  rounds = 0
  while True:
    rounds += 1
    smoothPrint('--- Round {} ---'.format(rounds))
    smoothPrint('you: {} monster: {}'.format(
        round(w.g.health * COEFFS['health'], 1), round(w.enemyState.health * COEFFS['health'], 1)))
    smoothPrint()

    # possible attack actions
    actions = {
        'attack': lambda w: EventPipe(w, SimpleAttackEvent),
        'strong attack': lambda w: EventPipe(w, SimpleAttackEvent),
        'hold': lambda w: EventPipe(w, SimpleAttackEvent),
        'change weapon': lambda w: EventPipe(w, SimpleAttackEvent),
        'change thing': lambda w: EventPipe(w, SimpleAttackEvent),
    }

    # get action name
    actionName = ''
    actionName = input('Enter fight action: ')

    while not actionName in actions:
      smoothPrint('No such action')
      actionName = input('Enter fight action: ')

    print()

    # set monster as target and gopher as attacker
    w = w._replace(targetState=w.enemyState, attackerState=w.g, attackerName=w.g.name)

    # perform attack on monster
    showStory('You attack Slug', True)
    monsterBefore = deepcopy(w.enemyState)
    w = actions[actionName](w)

    # change monster's state
    w = w._replace(enemyState=w.targetState)

    showChangedProps(monsterBefore, w.enemyState, prefix='monster\'s ')  # , postPrint=False)

    # check if monster is dead
    if w.enemyState.health <= 0:
      smoothPrint('monster defeated')
      w = w._replace(g=w.g._replace(fame=w.g.fame + 0.1))
      break

    # now set gopher as target and monster as attacker
    w = w._replace(targetState=w.g, attackerState=w.enemyState, attackerName='Slug')

    # perform attack on gopher
    gopherBefore = deepcopy(w.g)
    showStory('Slug attacks you', True)
    w = actions['attack'](w)

    # change gopher's state
    w = w._replace(g=w.targetState)

    print()
    showChangedProps(gopherBefore, w.g, prefix='your ')

    if w.g.health <= 0:
      smoothPrint('you defeated')
      break

  print()
  showChangedProps(gopherBefore, w.g)

  return (w, None)
