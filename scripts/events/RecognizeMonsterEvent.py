from random import randint
from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventFunc
from scripts.Assets import showRollResult, rollDice
from scripts.visual.Methods import showStory
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.ConsoleColors import bcolors
from scripts.visual.Converter import COEFFS
from scripts.Constants import (
    CONSIDER_MIN_BOUND,
    CONSIDER_MEDIUM_BOUND,
    CONSIDER_FULL_BOUND,
)
from texts.events import RecognizeMonsterTexts

# import possible events
from scripts.events.FloodEvent import FloodEvent
from scripts.events.DownfallEvent import DownfallEvent


def RecognizeMonsterEvent(w):
  return EventFunc(
      w,
      lambda w: w,
      RecognizeMonsterTexts,
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
  showStory(w.enemyType.minDescription())
  return (w, None)


def displayMediumDescription(w):
  showStory(w.enemyType.mediumDescription())
  return (w, None)


def displayFullDescription(w):
  showStory(w.enemyType.fullDescription())
  return (w, None)


def __calcDice__(w):
  d = w.g.intelligence * COEFFS['intelligence']
  string = '''
    your intelligence: {}{}{}
    min discription: {}int < {}{}
    medium discription: {}int < {}{}
    full discription: {}int < {}{}
  '''.format(
      bcolors.BOLD,
      d,
      bcolors.ENDC,
      bcolors.BOLD,
      CONSIDER_MIN_BOUND,
      bcolors.ENDC,
      bcolors.BOLD,
      CONSIDER_MEDIUM_BOUND,
      bcolors.ENDC,
      bcolors.BOLD,
      CONSIDER_FULL_BOUND,
      bcolors.ENDC,
  )
  showStory(string)

  return d
