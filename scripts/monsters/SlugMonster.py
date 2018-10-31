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

from scripts.inventory.GooArmor import GooArmor
from scripts.inventory.GooSlap import GooSlap

HEALTH_POINTS = 0.3
EVASION_POINTS = 0.07
FIGHTING_LEVEL = 5
DICE = 10

SlugState = namedtuple('SlugState', [
    'health',
    'evasion',
    'fightingLevel',
    'equipement',
])


def init():
  return SlugState(
      health=HEALTH_POINTS,
      evasion=EVASION_POINTS,
      fightingLevel=FIGHTING_LEVEL,
      equipement=[GooArmor(), GooSlap()]
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
