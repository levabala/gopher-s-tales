from classes.Event import __EventFunc__
from classes.Assets import d20
from texts.events import TradeTexts
from classes.Constants import *


def TradeEvent(rt):
  return __EventFunc__(
      rt,
      TradeTexts,
      lambda rt: d20() + rt.g.tradingLevel,
      TRADE_EVENT_FAILURE_CRIT_BOUND,
      TRADE_EVENT_FAILURE_SIMPLE_BOUND,
      TRADE_EVENT_SUCCESS_SIMPLE_BOUND,
      TRADE_EVENT_SUCCESS_CRIT_BOUND,
      lambda rt: rt._replace(g=rt.g._replace(
          wealth=rt.g.wealth - rt.w.yourBet
      )),
      lambda rt: rt._replace(g=rt.g._replace(
          wealth=rt.g.wealth + WEEK_TAX / 7
      )),
      lambda rt: rt._replace(g=rt.g._replace(
          wealth=rt.g.wealth + rt.w.yourBet * (1 / 3)
      )),
      lambda rt: rt._replace(g=rt.g._replace(
          wealth=rt.g.wealth + rt.w.yourBet * (3 / 3)
      )),
  )
