from scripts.WorldMethods import getArea
from scripts.events.Event import EventTrivialFunc
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showStory
from scripts.EventPipe import EventPipe
from scripts.Assets import rollDice
from texts.events import EmptyTexts
from scripts.Constants import (
    LIGHT_DAMAGE_COEFF,
    FULL_DAMAGE_COEFF,
    CRIT_DAMAGE_COEFF,
)

from scripts.events.ConsiderMonsterEvent import ConsiderMonsterEvent


def FightEvent(w):
  return EventTrivialFunc(
      w,
      EmptyTexts,
      _process
  )


def _process(w):
  w = EventPipe(w, ConsiderMonsterEvent)

  monsterState = w.enemy.init()

  while w.g.health > 0 and monsterState.hp > 0:
    evasion = monsterState.evasion

    # def attack(gopher, monsterState):

    actions = {
        'attack',
        'strong attack',
        'hold',
        'change weapon',
        'change thing'
    }

    attackPoints = rollDice(10) + w.g.fightingLevel

    input('do do do? ')

    if attackPoints < evasion * 0.8:
      w.enemy.takeDamage(monsterState, 0)
      smoothPrint('miss')
    elif attackPoints < evasion:
      w.enemy.takeDamage(monsterState, attackPoints * LIGHT_DAMAGE_COEFF)
      smoothPrint('light damage')
    elif attackPoints < evasion * 1.5:
      smoothPrint('full damage')
      w.enemy.takeDamage(monsterState, attackPoints * FULL_DAMAGE_COEFF)
    else:
      smoothPrint('crit damage')
      w.enemy.takeDamage(monsterState, attackPoints * CRIT_DAMAGE_COEFF)

  return (w, None)
