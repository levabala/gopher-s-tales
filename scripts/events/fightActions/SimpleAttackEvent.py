from math import tanh, pow
from random import randint
from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventFunc
from scripts.Assets import showRollResult, showRollResultAttack, rollDice
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
from scripts.GopherMethods import sumArmor
from scripts.inventory.NoWeapon import NoWeapon


def SimpleAttackEvent(w):
  return EventFunc(
      w,
      __preCalc__,
      SimpleAttackTexts,
      __calcDice__,
      w.targetState.evasion * MISS_DAMAGE_EVASION_COEFF,
      w.targetState.evasion * LIGHT_DAMAGE_EVASION_COEFF,
      w.targetState.evasion * FULL_DAMAGE_EVASION_COEFF,
      w.targetState.evasion * CRIT_DAMAGE_EVASION_COEFF,
      lambda w: (takeDamage(w, 0), None),
      lambda w: (takeDamage(w, w.attackPoints * LIGHT_DAMAGE_COEFF), None),
      lambda w: (takeDamage(w, w.attackPoints * FULL_DAMAGE_COEFF), None),
      lambda w: (takeDamage(w, w.attackPoints * CRIT_DAMAGE_COEFF), None),
  )


def __preCalc__(w):
  noWeapon = NoWeapon()

  weapon = next(
      (wea for wea in w.attackerState.equipement if wea['type'] == 'weapon'),
      noWeapon
  )
  dice = rollDice(*weapon['dice'])

  armor = sumArmor(w.targetState)
  attackProp = max(armor.items(), key=lambda a: a[1] - weapon[a[0]])
  coeff = 1 + tanh(attackProp[1] / 10) ** (1 / 3)

  attackPoints = coeff * (dice + w.attackerState.fightingLevel)

  prop = attackProp[0]
  showRollResultAttack(
      w.attackerName,
      '1 + tanh({}[{}] - {}[{}])^(1 / 3) = {}'.format(
          weapon[prop],
          prop,
          armor[prop],
          prop,
          round(coeff)
      ),
      '{} * ({} + {})'.format(round(coeff, 2), dice, w.attackerState.fightingLevel),
      'coeff + d{}x{} + fightingLevel'.format(*weapon['dice']),
      attackPoints,
      w.targetState.evasion * COEFFS['health'] * MISS_DAMAGE_EVASION_COEFF,
      w.targetState.evasion * COEFFS['health'] * LIGHT_DAMAGE_EVASION_COEFF,
      w.targetState.evasion * COEFFS['health'] * FULL_DAMAGE_EVASION_COEFF,
  )

  attackPoints /= COEFFS['health']

  return w._replace(attackPoints=attackPoints)


def __calcDice__(w):
  return w.attackPoints
