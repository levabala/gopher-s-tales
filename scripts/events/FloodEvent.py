from scripts.events.Event import EventFunc
from scripts.Assets import rollDice
from texts.events import FloodTexts
from scripts.Constants import (
    FLOOD_EVENT_FAILURE_CRIT_BOUND,
    FLOOD_EVENT_FAILURE_SIMPLE_BOUND,
    FLOOD_EVENT_SUCCESS_SIMPLE_BOUND,
    FLOOD_EVENT_ESCAPE_COEFF,
    FLOOD_EVENT_CRIT_HOLE_REDUCTION,
    FLOOD_EVENT_SIMPLE_HOLE_REDUCTION,
)


def FloodEvent(w):
  return EventFunc(
      w,
      lambda w: w,
      FloodTexts,
      lambda w: rollDice(20) + FLOOD_EVENT_ESCAPE_COEFF * w.g.agility,
      FLOOD_EVENT_FAILURE_CRIT_BOUND,
      FLOOD_EVENT_FAILURE_SIMPLE_BOUND,
      FLOOD_EVENT_SUCCESS_SIMPLE_BOUND,
      FLOOD_EVENT_SUCCESS_SIMPLE_BOUND,  # the save as previous
      lambda w: (w._replace(g=w.g._replace(
          holeDeep=w.g.holeDeep - FLOOD_EVENT_CRIT_HOLE_REDUCTION,
      )), None),
      lambda w: (w._replace(g=w.g._replace(
          holeDeep=w.g.holeDeep - FLOOD_EVENT_SIMPLE_HOLE_REDUCTION,
      )), None),
      lambda w: (w, None),
      lambda w: (w, None),
      showChangedPropsAfterAll=True
  )
