from classes.Event import __EventFunc__
from classes.Assets import d20
from texts.events import DownfallTexts
from classes.Constants import *


def DownfallEvent(rt):
  __EventFunc__(
      rt,
      DownfallTexts,
      lambda rt: d20() + DOWNFALL_EVENT_ESCAPE_COEFF * rt.g.strenght,
      DOWNFALL_EVENT_FAILURE_CRIT_BOUND,
      DOWNFALL_EVENT_FAILURE_SIMPLE_BOUND,
      DOWNFALL_EVENT_SUCCESS_SIMPLE_BOUND,
      DOWNFALL_EVENT_SUCCESS_SIMPLE_BOUND,  # the save as previous
      lambda rt: rt._replace(g=rt.g._replace(
          holeDeep=rt.g.holeDeep - DOWNFALL_EVENT_CRIT_HOLE_REDUCTION,
          health=rt.g.health - DOWNFALL_EVENT_CRIT_GOPHER_DAMAGE
      )),
      lambda rt: rt._replace(g=rt.g._replace(
          holeDeep=rt.g.holeDeep - DOWNFALL_EVENT_SIMPLE_HOLE_REDUCTION,
          health=rt.g.health - DOWNFALL_EVENT_SIMPLE_GOPHER_DAMAGE
      )),
      lambda rt: rt,
      lambda rt: rt,
  )
