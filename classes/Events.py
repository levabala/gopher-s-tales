from classes.Assets import d20
from classes.SmoothPrint import smoothPrint
from classes.Constants import *
from classes.GopherVisual import (
    CRITICAL_FAILURE,
    SIMPLE_FAILURE,
    SIMPLE_SUCCESS,
    showStory
)


def floodEvent(gopher):
  showStory('\nOhhhh! FLOODING!!!')
  showStory('You\'re trying to escape the water...\n')

  d = d20() + FLOOD_EVENT_ESCAPE_COEFF * gopher.agility

  if d < FLOOD_EVENT_FAILURE_CRIT_BOUND:
    smoothPrint(CRITICAL_FAILURE)
    showStory('You\'ve not time to react on this!')
    showStory('Frrrrr... You\'re completly wet')
    showStory('\nA huge part of the hole was flooded')
    gopher._replace(
        holeDeep=gopher.holeDeep - FLOOD_EVENT_CRIT_HOLE_REDUCTION,
    )
    return gopher
  elif d < FLOOD_EVENT_FAILURE_SIMPLE_BOUND:
    smoothPrint(SIMPLE_FAILURE)
    showStory('\nYour legs are a bit wet')
    showStory('And the hole a bit flooded...')
    gopher._replace(
        holeDeep=gopher.holeDeep - FLOOD_EVENT_SIMPLE_HOLE_REDUCTION,
    )
    return gopher
  elif d < FLOOD_EVENT_SUCCESS_SIMPLE_BOUND:
    smoothPrint(SIMPLE_SUCCESS)
    showStory('\nYou\'ve escaped beating water!')
    showStory('Just a little water...')
    return gopher

  # should be never
  raise Exception('very strange dice')


def downFallEvent(gopher):
  showStory('\nOhhhh! DOWNFALL!!!')
  showStory('You\'re trying to jump off falling roof...\n')

  d = d20() + FLOOD_EVENT_ESCAPE_COEFF * gopher.agility

  if d < DOWNFALL_EVENT_FAILURE_CRIT_BOUND:
    smoothPrint(CRITICAL_FAILURE, SMALL_DELAY)
    showStory('\nAuch! Falling stones have damaged you!')
    showStory('And the hole is littered!')
    gopher._replace(
        holeDeep=gopher.holeDeep - DOWNFALL_EVENT_CRIT_HOLE_REDUCTION,
        health=gopher.health - DOWNFALL_EVENT_CRIT_GOPHER_DAMAGE
    )
    return gopher
  elif d < DOWNFALL_EVENT_FAILURE_SIMPLE_BOUND:
    smoothPrint(SIMPLE_FAILURE, SMALL_DELAY)
    showStory('\nOne little stone hurts you arm. Nothing critical...')
    showStory('And the hole becomes a bit less deep!')
    gopher._replace(
        holeDeep=gopher.holeDeep - DOWNFALL_EVENT_SIMPLE_HOLE_REDUCTION,
        health=gopher.health - DOWNFALL_EVENT_SIMPLE_GOPHER_DAMAGE
    )
    return gopher
  elif d < DOWNFALL_EVENT_SUCCESS_SIMPLE_BOUND:
    smoothPrint(SIMPLE_SUCCESS, SMALL_DELAY)
    showStory('\nJust sand. whew')
    return gopher

  # should be never
  raise Exception('very strange dice')
