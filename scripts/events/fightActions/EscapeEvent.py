from random import random
from scripts.events.EndDayEvent import EndDayEvent
from scripts.events.Event import EventTrivialFunc
from scripts.visual.Methods import showStory, green
from scripts.WorldMethods import takeDamage
from texts.events import EscapeTexts

from scripts.Constants import ESCAPE_BASE_CHANCE, ESCAPE_FAIL_DAMAGE


def EscapeEvent(w):
  return EventTrivialFunc(
      w,
      EscapeTexts,
      _process,
  )


def _process(w):
  seed = random()
  if seed < ESCAPE_BASE_CHANCE:
    showStory('You escaped the figth', True)
    w = w._replace(escapedFight=True)
  else:
    showStory('You tried to escape but got a hit into your back', True)

    realAttacker = w.attackerState
    realTarget = w.targetState

    # now set escaper as target and opponent as attacker
    w = w._replace(
        targetState=realAttacker,
        attackerState=realTarget,
        attackerName=realTarget.name
    )

    w = takeDamage(w, ESCAPE_FAIL_DAMAGE)

    # and switch back
    w = w._replace(
        targetState=w.attackerState,
        attackerState=w.targetState,
        attackerName=w.targetState.name
    )

  return (w, None)
