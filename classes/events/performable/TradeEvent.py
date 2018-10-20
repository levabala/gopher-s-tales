from classes.Event import __EventFunc__
from classes.Assets import d20
from texts.events import TradeTexts
from classes.Constants import *


def TradeEvent(rt):
  __EventFunc__(
      rt,
      TradeTexts,
      lambda rt: d20() + rt.g.trading,
      TRADE_EVENT_FAILURE_CRIT_BOUND,
      TRADE_EVENT_FAILURE_SIMPLE_BOUND,
      TRADE_EVENT_SUCCESS_SIMPLE_BOUND,
      TRADE_EVENT_SUCCESS_CRIT_BOUND,
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
