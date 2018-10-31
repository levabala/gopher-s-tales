from random import randint
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
    MISS_DAMAGE_EVASION_COEFF,
    LIGHT_DAMAGE_EVASION_COEFF,
    FULL_DAMAGE_EVASION_COEFF,
    CRIT_DAMAGE_EVASION_COEFF,
)
from texts.events import SimpleAttackTexts


def SimpleAttackEvent(w):
  return EventFunc(
      w,
      __preCalc__,
      SimpleAttackTexts,
      __calcDice__,
      w.targetState.evasion * MISS_DAMAGE_EVASION_COEFF,
      w.targetState.evasion * LIGHT_DAMAGE_COEFF,
      w.targetState.evasion * FULL_DAMAGE_COEFF,
      w.targetState.evasion * CRIT_DAMAGE_EVASION_COEFF,
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
      w.targetState.evasion * COEFFS['health'] * MISS_DAMAGE_EVASION_COEFF,
      w.targetState.evasion * COEFFS['health'] * LIGHT_DAMAGE_EVASION_COEFF,
      w.targetState.evasion * COEFFS['health'] * FULL_DAMAGE_EVASION_COEFF,
  )

  attackPoints /= COEFFS['health']

  return w._replace(attackPoints=attackPoints)


def __calcDice__(w):
  return w.attackPoints
