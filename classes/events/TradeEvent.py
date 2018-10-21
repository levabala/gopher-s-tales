from classes.Event import __EventFunc__
from classes.Assets import rollDice, showRollResult
from texts.events import TradeTexts
from classes.Constants import *


def TradeEvent(rt):
  return __EventFunc__(
      rt,
      TradeTexts,
      __calcDice__,
      TRADE_EVENT_FAILURE_CRIT_BOUND,
      TRADE_EVENT_FAILURE_SIMPLE_BOUND,
      TRADE_EVENT_SUCCESS_SIMPLE_BOUND,
      TRADE_EVENT_SUCCESS_CRIT_BOUND,
      lambda rt: rt._replace(g=rt.g._replace(
          wealth=rt.g.wealth - rt.w.yourBet,
          actionPoints=rt.g.actionPoints - 1
      )),
      lambda rt: rt._replace(g=rt.g._replace(
          wealth=rt.g.wealth + WEEK_TAX / 7,
          actionPoints=rt.g.actionPoints - 1
      )),
      lambda rt: rt._replace(g=rt.g._replace(
          wealth=rt.g.wealth + rt.w.yourBet * (1 / 3),
          actionPoints=rt.g.actionPoints - 1
      )),
      lambda rt: rt._replace(g=rt.g._replace(
          wealth=rt.g.wealth + rt.w.yourBet * (3 / 3),
          actionPoints=rt.g.actionPoints - 1
      )),
  )


def __calcDice__(rt):
  dice = rollDice(20)
  d = dice + rt.g.tradingLevel
  showRollResult([dice, rt.g.tradingLevel], ['d20', 'tradingLevel'],
                 TRADE_EVENT_SUCCESS_SIMPLE_BOUND)
  return d
