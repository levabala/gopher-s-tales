from copy import deepcopy
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


def FightEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  w = EventPipe(w, RecognizeMonsterEvent)

  monsterState = w.enemy.init()

  gopherBefore = None
  rounds = 0
  while True:
    rounds += 1
    smoothPrint('--- Round {} ---'.format(rounds))
    smoothPrint()

    gopherBefore = deepcopy(w.g)

    actions = {
        'attack': simpleAttack,
        'strong attack': strongAttack,
        'hold': simpleAttack,
        'change weapon': simpleAttack,
        'change thing': simpleAttack,
    }

    actionName = ''
    actionName = input('Enter fight action: ')

    while not actionName in actions:
      smoothPrint('No such action')
      actionName = input('Enter fight action: ')

    print()

    monsterBefore = deepcopy(monsterState)
    monsterState = actions[actionName](w, monsterState)
    showChangedProps(monsterBefore, monsterState, prefix='monster\'s ')  # , postPrint=False)

    if monsterState.health <= 0:
      smoothPrint('monster defeated')
      w = w._replace(g=w.g._replace(fame=w.g.fame + 0.1))
      break

    w = w._replace(g=w.enemy.attack(monsterState, w.g))

    print()
    showChangedProps(gopherBefore, w.g, prefix='your ')

    if w.g.health <= 0:
      smoothPrint('you defeated')
      break

  print()
  showChangedProps(gopherBefore, w.g)

  return (w, None)


def strongAttack(w, monsterState):
  pass


def simpleAttack(w, monsterState):
  dice = rollDice(8)
  attackPoints = dice + w.g.fightingLevel

  showRollResult(
      YOU_STRING,
      [dice, w.g.fightingLevel],
      ['d8', 'fightingLevel'],
      monsterState.evasion * COEFFS['health'] * 0.8,
      monsterState.evasion * COEFFS['health'],
      monsterState.evasion * COEFFS['health'] * 1.5,
  )

  attackPoints /= COEFFS['health']

  if attackPoints < monsterState.evasion * 0.8:
    smoothPrint('miss')
    return w.enemy.takeDamage(monsterState, 0)
  elif attackPoints < monsterState.evasion:
    smoothPrint('light damage')
    return w.enemy.takeDamage(monsterState, attackPoints * LIGHT_DAMAGE_COEFF)
  elif attackPoints < monsterState.evasion * 1.5:
    smoothPrint('full damage')
    return w.enemy.takeDamage(monsterState, attackPoints * FULL_DAMAGE_COEFF)
  else:
    smoothPrint('crit damage')
    return w.enemy.takeDamage(monsterState, attackPoints * CRIT_DAMAGE_COEFF)
