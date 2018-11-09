from math import pow
from infinity import inf
from random import randint
from scripts.visual.ConsoleColors import bcolors, green, blue, bold
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
    HOLD_EVASION_COEFF,
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
      w.targetState.evasion * MISS_DAMAGE_EVASION_COEFF *
      (HOLD_EVASION_COEFF if w.targetState.holdTurnsLeft > 0 else 1),
      w.targetState.evasion * LIGHT_DAMAGE_EVASION_COEFF *
      (HOLD_EVASION_COEFF if w.targetState.holdTurnsLeft > 0 else 1),
      w.targetState.evasion * FULL_DAMAGE_EVASION_COEFF *
      (HOLD_EVASION_COEFF if w.targetState.holdTurnsLeft > 0 else 1),
      w.targetState.evasion * CRIT_DAMAGE_EVASION_COEFF *
      (HOLD_EVASION_COEFF if w.targetState.holdTurnsLeft > 0 else 1),
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
  # TODO: fix no-weapon bug
  weaponProps = {
      k: v for k, v in weapon.items()
      if k != 'equiped' and k != 'weight' and isinstance(v, (int, float)) and v > 0
  }
  dice = rollDice(*weapon['dice'])

  armor = sumArmor(w.targetState)
  diff = -inf
  weapons = list(weaponProps.items())
  prop = weapons[0]
  for wea in weapons:
    d = wea[1] - armor[wea[0]]
    if d > diff:
      diff = d
      prop = wea

  attackProp = prop
  coeff = getAttackCoeff(diff)

  attackPoints = coeff * (dice + w.attackerState.fightingLevel)

  prop = attackProp[0]
  showStory('{} performs a simple attack by {}'.format(
      w.attackerName,
      blue(weapon['name']),
  ), True)

  if w.targetState.holdTurnsLeft > 0:
    showStory('Target\'s evasion multiplied by {}% because of holding'.format(
        green(round((HOLD_EVASION_COEFF - 1) * 100))
    ), True)

  showRollResultAttack(
      w.attackerName,
      '{} (because of max diff {} in {})'.format(
          green(round(coeff, 2)),
          green(diff),
          green(prop),
      ),
      '{} * ({} + {})'.format(
          green(round(coeff, 2)),
          green(dice),
          green(w.attackerState.fightingLevel)
      ),
      '{} * (d{}x{} + {})'.format(
          'coeff',
          green(weapon['dice'][0]),
          green(weapon['dice'][1]),
          'fightingLevel',
      ),
      attackPoints,
      w.targetState.evasion * COEFFS['health'] * MISS_DAMAGE_EVASION_COEFF *
      (HOLD_EVASION_COEFF if w.targetState.holdTurnsLeft > 0 else 1),
      w.targetState.evasion * COEFFS['health'] * LIGHT_DAMAGE_EVASION_COEFF *
      (HOLD_EVASION_COEFF if w.targetState.holdTurnsLeft > 0 else 1),
      w.targetState.evasion * COEFFS['health'] * FULL_DAMAGE_EVASION_COEFF *
      (HOLD_EVASION_COEFF if w.targetState.holdTurnsLeft > 0 else 1),
  )

  attackPoints /= COEFFS['health']

  return w._replace(
      attackPoints=attackPoints,
      g=w.g._replace(holdTurnsLeft=0),
  )


def __calcDice__(w):
  return w.attackPoints
