from random import randint
from infinity import inf
from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventFunc
from scripts.Assets import showRollResult, rollDice
from scripts.visual.Converter import COEFFS
from scripts.WorldMethods import takeDamage
from scripts.Constants import (
    LIGHT_DAMAGE_COEFF,
    FULL_DAMAGE_COEFF,
    CRIT_DAMAGE_COEFF,
    YOU_STRING,
)
from texts.events import SimpleAttackTexts


def SimpleAttackEvent(w):
  return EventFunc(
      w,
      __preCalc__,
      SimpleAttackTexts,
      __calcDice__,
      w.targetState.evasion * 0.8,
      w.targetState.evasion,
      w.targetState.evasion * 1.5,
      inf,
      lambda w: (takeDamage(w, 0), None),
      lambda w: (takeDamage(w, w.attackPoints * LIGHT_DAMAGE_COEFF), None),
      lambda w: (takeDamage(w, w.attackPoints * FULL_DAMAGE_COEFF), None),
      lambda w: (takeDamage(w, w.attackPoints * CRIT_DAMAGE_COEFF), None),
  )


def __preCalc__(w):
  dice = rollDice(8)
  attackPoints = dice + w.attackerState.fightingLevel

  showRollResult(
      w.attackerName,
      [dice, w.attackerState.fightingLevel],
      ['d' + str(dice), 'fightingLevel'],
      w.targetState.evasion * COEFFS['health'] * 0.8,
      w.targetState.evasion * COEFFS['health'],
      w.targetState.evasion * COEFFS['health'] * 1.5,
  )

  attackPoints /= COEFFS['health']

  return w._replace(attackPoints=attackPoints)


def __calcDice__(w):
  return w.attackPoints
