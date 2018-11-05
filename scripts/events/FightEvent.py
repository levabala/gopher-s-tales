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
from scripts.GopherMethods import spendActionPoint
from scripts.Completer import requestCompletableInputStrict
from scripts.Constants import (
    LIGHT_DAMAGE_COEFF,
    FULL_DAMAGE_COEFF,
    CRIT_DAMAGE_COEFF,
    YOU_STRING,
)

from scripts.events.RecognizeMonsterEvent import RecognizeMonsterEvent
from scripts.events.fightActions.SimpleAttackEvent import SimpleAttackEvent
from scripts.events.fightActions.StrongAttackEvent import StrongAttackEvent
from scripts.events.performable.EquipItemEvent import EquipItemEvent
from scripts.events.performable.UnequipItemEvent import UnequipItemEvent


def FightEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  w = EventPipe(w, RecognizeMonsterEvent)

  w = w._replace(enemyState=w.enemyType.init())

  rounds = 0
  gopherInBegging = deepcopy(w.g)
  while True:
    gopherBefore = deepcopy(w.g)

    rounds += 1
    smoothPrint('--- Round {} ---'.format(rounds))
    smoothPrint('you: {} monster: {}'.format(
        round(w.g.health * COEFFS['health'], 1), round(w.enemyState.health * COEFFS['health'], 1)))
    smoothPrint()

    # possible attack actions
    actions = {
        'attack': lambda w: EventPipe(w, SimpleAttackEvent),
        'strong attack': lambda w: EventPipe(w, StrongAttackEvent),
        'hold': lambda w: EventPipe(w, SimpleAttackEvent),
        'change weapon': lambda w: EventPipe(w, SimpleAttackEvent),
        'change thing': lambda w: EventPipe(w, SimpleAttackEvent),
        'equip': lambda w: EventPipe(w, EquipItemEvent),
        'unequip': lambda w: EventPipe(w, UnequipItemEvent),
    }

    # get action name
    actionName = requestCompletableInputStrict(
        options=actions.keys(),
        requestString='Enter fight action: ',
        wrongInputString='No such fight action'
    )

    print()

    # set monster as target and gopher as attacker
    w = w._replace(targetState=w.enemyState, attackerState=w.g, attackerName=w.g.name)

    # perform attack on monster
    monsterBefore = deepcopy(w.enemyState)
    w = actions[actionName](w)

    # change monster's state
    w = w._replace(enemyState=w.targetState)

    print()
    showChangedProps(monsterBefore, w.enemyState, prefix='monster\'s ')  # , postPrint=False)

    # check if monster is dead
    if w.enemyState.health <= 0:
      smoothPrint('monster defeated')
      w = w._replace(g=w.g._replace(fame=w.g.fame + 0.1))
      break

    input('Press Enter...\n')

    # now set gopher as target and monster as attacker
    w = w._replace(targetState=w.g, attackerState=w.enemyState, attackerName='Slug')

    # perform attack on gopher
    w = actions['attack'](w)

    # change gopher's state
    w = w._replace(g=w.targetState)

    print()
    showChangedProps(gopherBefore, w.g, prefix='your ')

    if w.g.health <= 0:
      smoothPrint('you defeated')
      break

  print()
  w = spendActionPoint(w)

  showChangedProps(gopherInBegging, w.g)

  return (w, None)
