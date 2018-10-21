from classes.Event import __EventFunc__
from classes.Assets import rollDice
from texts.events import FloodTexts
from classes.Constants import *


def FloodEvent(rt):
  return __EventFunc__(
      rt,
      FloodTexts,
      lambda rt: rollDice(20) + FLOOD_EVENT_ESCAPE_COEFF * rt.g.agility,
      FLOOD_EVENT_FAILURE_CRIT_BOUND,
      FLOOD_EVENT_FAILURE_SIMPLE_BOUND,
      FLOOD_EVENT_SUCCESS_SIMPLE_BOUND,
      FLOOD_EVENT_SUCCESS_SIMPLE_BOUND,  # the save as previous
      lambda rt: rt._replace(g=rt.g._replace(
          holeDeep=rt.g.holeDeep - FLOOD_EVENT_CRIT_HOLE_REDUCTION,
      )),
      lambda rt: rt._replace(g=rt.g._replace(
          holeDeep=rt.g.holeDeep - FLOOD_EVENT_SIMPLE_HOLE_REDUCTION,
      )),
      lambda rt: rt,
      lambda rt: rt,
  )
