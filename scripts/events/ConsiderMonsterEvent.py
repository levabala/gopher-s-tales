from random import randint
from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventFunc
from scripts.Assets import showRollResult, rollDice
from scripts.visual.Methods import showStory
from scripts.Constants import (
    CONSIDER_MIN_BOUND,
    CONSIDER_MEDIUM_BOUND,
    CONSIDER_FULL_BOUND,
)
from texts.events import ConsiderMonsterTexts

# import possible events
from scripts.events.FloodEvent import FloodEvent
from scripts.events.DownfallEvent import DownfallEvent


def ConsiderMonsterEvent(w):
  return EventFunc(
      w,
      lambda w: w,
      ConsiderMonsterTexts,
      __calcDice__,
      CONSIDER_MIN_BOUND,
      CONSIDER_MEDIUM_BOUND,
      CONSIDER_FULL_BOUND,
      CONSIDER_FULL_BOUND,
      displayMinDescription,
      displayMediumDescription,
      displayFullDescription,
      lambda w: (w, None),
  )


def displayMinDescription(w):
  showStory(w.enemy.minDescription())
  return (w, None)


def displayMediumDescription(w):
  showStory(w.enemy.mediumDescription())
  return (w, None)


def displayFullDescription(w):
  showStory(w.enemy.fullDescription())
  return (w, None)


def __calcDice__(w):
  d = w.g.intelligence
  showRollResult([d], ['intelligence'], CONSIDER_MEDIUM_BOUND)

  return d
