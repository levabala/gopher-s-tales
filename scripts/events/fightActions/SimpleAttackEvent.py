from math import pow
from random import randint
from scripts.visual.ConsoleColors import bcolors, green, blue
from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventFunc
from scripts.Assets import showRollResult, showRollResultAttack, rollDice
from scripts.visual.Methods import showStory
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
from scripts.GopherMethods import sumArmor, getAttackCoeff
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
  weaponProps = {k: v for k, v in weapon.items() if isinstance(v, (int, float)) and v > 0}
  dice = rollDice(*weapon['dice'])

  armor = sumArmor(w.targetState)
  attackProp = max(weaponProps.items(), key=lambda a: armor[a[0]] - a[1])
  coeff = getAttackCoeff(attackProp[1])

  attackPoints = coeff * (dice + w.attackerState.fightingLevel)

  prop = attackProp[0]
  showStory('{} performs a simple attack by {}'.format(
      w.attackerName,
      blue(weapon['name']),
  ), True)
  showRollResultAttack(
      w.attackerName,
      '{} (because of max diff {} in {})'.format(
          green(round(coeff, 2)),
          green(attackProp[1]),
          green(prop),
      ),
      '{} * ({} + {})'.format(
          green(round(coeff, 2)),
          green(dice),
          green(w.attackerState.fightingLevel)
      ),
      'coeff * (d{}x{} + fightingLevel)'.format(
          green(weapon['dice'][0]),
          green(weapon['dice'][1]),
      ),
      attackPoints,
      w.targetState.evasion * COEFFS['health'] * MISS_DAMAGE_EVASION_COEFF,
      w.targetState.evasion * COEFFS['health'] * LIGHT_DAMAGE_EVASION_COEFF,
      w.targetState.evasion * COEFFS['health'] * FULL_DAMAGE_EVASION_COEFF,
  )

  attackPoints /= COEFFS['health']

  return w._replace(attackPoints=attackPoints)


def __calcDice__(w):
  return w.attackPoints
