from collections import namedtuple
import texts.monsters.SlugTexts as SlugTexts

MAX_HIT_POINTS = 1
EVASION_POINTS = 0.1

SlugState = namedtuple('SlugState', [
    'hp',
    'evasion',
])


def init():
  return SlugState(
      hp=MAX_HIT_POINTS,
      evasion=EVASION_POINTS
  )


def minDescription():
  return SlugTexts.MIN_DESCRIPTION


def mediumDescription():
  return SlugTexts.MEDIUM_DESCRIPTION


def fullDescription():
  return SlugTexts.FULL_DESCRIPTION


def takeDamage(state, damage):
  pass


def attack(state, gopher):
  pass
