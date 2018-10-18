from classes.Assets import d20
from classes.SmoothPrint import smoothPrint
from classes.Constants import *
from texts.events import FloodTexts, DownfallTexts
from classes.GopherVisual import (
    CRITICAL_FAILURE,
    SIMPLE_FAILURE,
    SIMPLE_SUCCESS,
    showStory
)


def floodEvent(gopher):
  showStory(FloodTexts.INIT)

  d = d20() + FLOOD_EVENT_ESCAPE_COEFF * gopher.agility

  if d < FLOOD_EVENT_FAILURE_CRIT_BOUND:
    smoothPrint(CRITICAL_FAILURE)
    showStory(FloodTexts.FAILURE_CRIT)
    gopher._replace(
        holeDeep=gopher.holeDeep - FLOOD_EVENT_CRIT_HOLE_REDUCTION,
    )
    return gopher
  elif d < FLOOD_EVENT_FAILURE_SIMPLE_BOUND:
    smoothPrint(SIMPLE_FAILURE)
    showStory(FloodTexts.FAILURE_SIMPLE)
    gopher._replace(
        holeDeep=gopher.holeDeep - FLOOD_EVENT_SIMPLE_HOLE_REDUCTION,
    )
    return gopher
  elif d < FLOOD_EVENT_SUCCESS_SIMPLE_BOUND:
    smoothPrint(SIMPLE_SUCCESS)
    showStory(FloodTexts.SUCCESS_SIMPLE)
    return gopher

  # should be never
  raise Exception('very strange dice')


def downFallEvent(gopher):
  showStory(DownfallTexts.INIT)

  d = d20() + FLOOD_EVENT_ESCAPE_COEFF * gopher.agility

  if d < DOWNFALL_EVENT_FAILURE_CRIT_BOUND:
    smoothPrint(CRITICAL_FAILURE, SMALL_DELAY)
    showStory(DownfallTexts.FAILURE_CRIT)
    gopher._replace(
        holeDeep=gopher.holeDeep - DOWNFALL_EVENT_CRIT_HOLE_REDUCTION,
        health=gopher.health - DOWNFALL_EVENT_CRIT_GOPHER_DAMAGE
    )
    return gopher
  elif d < DOWNFALL_EVENT_FAILURE_SIMPLE_BOUND:
    smoothPrint(SIMPLE_FAILURE, SMALL_DELAY)
    showStory(DownfallTexts.FAILURE_SIMPLE)
    gopher._replace(
        holeDeep=gopher.holeDeep - DOWNFALL_EVENT_SIMPLE_HOLE_REDUCTION,
        health=gopher.health - DOWNFALL_EVENT_SIMPLE_GOPHER_DAMAGE
    )
    return gopher
  elif d < DOWNFALL_EVENT_SUCCESS_SIMPLE_BOUND:
    smoothPrint(SIMPLE_SUCCESS, SMALL_DELAY)
    showStory(DownfallTexts.SUCCESS_SIMPLE)
    return gopher

  # should be never
  raise Exception('very strange dice')
