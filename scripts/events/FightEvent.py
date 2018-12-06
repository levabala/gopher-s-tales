from copy import deepcopy
from scripts.EventPipe import EventPipe
from scripts.WorldMethods import getArea, getCurrentArea
from scripts.events.Event import EventTrivialFunc
from scripts.events.DieEvent import DieEvent
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
from scripts.events.fightActions.EscapeEvent import EscapeEvent
from scripts.events.fightActions.HoldEvent import HoldEvent
from scripts.events.performable.EquipItemEvent import EquipItemEvent
from scripts.events.performable.UnequipItemEvent import UnequipItemEvent


def FightEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  w = w._replace(
      # enemyState=w.enemyType.init(),
      escapedFight=False,
  )

  w = EventPipe(w, RecognizeMonsterEvent)

  rounds = 0
  gopherInBegging = deepcopy(w.g)
  while True:
    gopherBefore = deepcopy(w.g)

    w = w._replace(g=w.g._replace(holdTurnsLeft=max(w.g.holdTurnsLeft - 1, 0)))

    rounds += 1
    smoothPrint('--- Round {} ---'.format(rounds))
    smoothPrint('you: {} monster: {}'.format(
        round(w.g.health * COEFFS['health'], 1), round(w.enemyState.health * COEFFS['health'], 1)))
    smoothPrint()

    # possible attack actions
    actions = {
        'attack': lambda w: EventPipe(w, SimpleAttackEvent),
        'strong attack': lambda w: EventPipe(w, StrongAttackEvent),
        'hold': lambda w: EventPipe(w, HoldEvent),
        'escape': lambda w: EventPipe(w, EscapeEvent),
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

    # set monster as g=w.g._replace(holdTurnsLeft=0),target and gopher as attacker
    w = w._replace(targetState=w.enemyState, attackerState=w.g, attackerName=w.g.name)

    # perform attack on monster
    monsterBefore = deepcopy(w.enemyState)
    w = actions[actionName](w)

    # check if you escaped the situation
    if w.escapedFight:
      break

    # change monster's state
    w = w._replace(enemyState=w.targetState)

    print()
    showChangedProps(monsterBefore, w.enemyState, prefix='monster\'s ', )
    showChangedProps(gopherBefore, w.attackerState, prefix='gopher\'s ', printIfNothing=False)

    # check if monster is dead
    if w.enemyState.health <= 0:
      smoothPrint('monster defeated')
      w = w._replace(g=w.g._replace(fame=w.g.fame + 0.1))
      area = getCurrentArea(w)
      area['monsters count'] -= 1

      showStory('Monsters left: {}'.format(area['monsters count']), True)

      break

    input('Press Enter...\n')

    # now set gopher as target and monster as attacker
    w = w._replace(targetState=w.g, attackerState=w.enemyState, attackerName=w.enemyState.name)

    # perform attack on gopher
    w = actions['attack'](w)

    # check if monster escaped the situation
    if w.escapedFight:
      break

    # change gopher'sstate
    w = w._replace(g=w.targetState)

    print()
    showChangedProps(gopherBefore, w.g, prefix='your ')
    showChangedProps(monsterBefore, w.enemyState, prefix='monster\'s ', printIfNothing=False)

    if w.g.health <= 0:
      smoothPrint('you defeated')
      break

  print()

  smoothPrint('All after-fight changes:')
  showChangedProps(gopherInBegging, w.g)

  if w.g.health <= 0:
    return (w, DieEvent)

  return (w, None)
