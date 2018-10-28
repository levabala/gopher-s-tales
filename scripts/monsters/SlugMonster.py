from collections import namedtuple
import texts.monsters.SlugTexts as SlugTexts
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showStory
from scripts.Assets import rollDice, showRollResult
from scripts.visual.Converter import COEFFS
from scripts.Constants import (
    LIGHT_DAMAGE_COEFF,
    FULL_DAMAGE_COEFF,
    CRIT_DAMAGE_COEFF,
    MONSTER_STRING,
)

HEALTH_POINTS = 0.3
EVASION_POINTS = 0.05
FIGHTING_LEVEL = 5
DICE = 10

SlugState = namedtuple('SlugState', [
    'health',
    'evasion',
    'fightingLevel',
])


def init():
  return SlugState(
      health=HEALTH_POINTS,
      evasion=EVASION_POINTS,
      fightingLevel=FIGHTING_LEVEL,
  )


def minDescription():
  return SlugTexts.MIN_DESCRIPTION


def mediumDescription():
  return SlugTexts.MEDIUM_DESCRIPTION


def fullDescription():
  return SlugTexts.FULL_DESCRIPTION


def takeDamage(w, damage):
  return w._replace(
      enemyState=w.enemyState._replace(
          health=w.enemyState.health - damage
      )
  )


def attack(state, gopher):
  showStory('Slug attacks you', True)

  dice = rollDice(DICE)
  attackPoints = dice + FIGHTING_LEVEL

  attackPoints /= COEFFS['health']

  showRollResult(
      MONSTER_STRING,
      [dice, FIGHTING_LEVEL],
      ['d' + str(DICE), 'fightingLevel'],
      gopher.evasion * COEFFS['health'] * 0.8,
      gopher.evasion * COEFFS['health'],
      gopher.evasion * COEFFS['health'] * 1.5,
  )

  if attackPoints < gopher.evasion * 0.8:
    smoothPrint('miss')
    return gopher._replace(health=gopher.health - 0)
  elif attackPoints < gopher.evasion:
    smoothPrint('light damage')
    return gopher._replace(health=gopher.health - attackPoints * LIGHT_DAMAGE_COEFF)
  elif attackPoints < gopher.evasion * 1.5:
    smoothPrint('full damage')
    return gopher._replace(health=gopher.health - attackPoints * FULL_DAMAGE_COEFF)
  else:
    smoothPrint('crit damage')
    return gopher._replace(health=gopher.health - attackPoints * CRIT_DAMAGE_COEFF)
