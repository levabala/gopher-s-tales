from scripts.events.Event import EventFunc
from scripts.Assets import rollDice
from texts.events import DownfallTexts
from scripts.Constants import (
    DOWNFALL_EVENT_ESCAPE_COEFF,
    DOWNFALL_EVENT_FAILURE_CRIT_BOUND,
    DOWNFALL_EVENT_FAILURE_SIMPLE_BOUND,
    DOWNFALL_EVENT_SUCCESS_SIMPLE_BOUND,
    DOWNFALL_EVENT_CRIT_HOLE_REDUCTION,
    DOWNFALL_EVENT_CRIT_GOPHER_DAMAGE,
    DOWNFALL_EVENT_SIMPLE_HOLE_REDUCTION,
    DOWNFALL_EVENT_SIMPLE_GOPHER_DAMAGE
)


def DownfallEvent(w):
  return EventFunc(
      w,
      lambda w: w,
      DownfallTexts,
      lambda w: rollDice(20) + DOWNFALL_EVENT_ESCAPE_COEFF * w.g.strenght,
      DOWNFALL_EVENT_FAILURE_CRIT_BOUND,
      DOWNFALL_EVENT_FAILURE_SIMPLE_BOUND,
      DOWNFALL_EVENT_SUCCESS_SIMPLE_BOUND,
      DOWNFALL_EVENT_SUCCESS_SIMPLE_BOUND,  # the save as previous
      lambda w: (w._replace(g=w.g._replace(
          holeDeep=w.g.holeDeep - DOWNFALL_EVENT_CRIT_HOLE_REDUCTION,
          health=w.g.health - DOWNFALL_EVENT_CRIT_GOPHER_DAMAGE
      )), None),
      lambda w: (w._replace(g=w.g._replace(
          holeDeep=w.g.holeDeep - DOWNFALL_EVENT_SIMPLE_HOLE_REDUCTION,
          health=w.g.health - DOWNFALL_EVENT_SIMPLE_GOPHER_DAMAGE
      )), None),
      lambda w: (w, None),
      lambda w: (w, None),
  )
