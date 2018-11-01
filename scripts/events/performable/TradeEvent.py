from scripts.events.EmptyEvent import EmptyEvent
from scripts.events.Event import EventFunc
from scripts.Assets import showRollResult, rollDice
from scripts.visual.ConsoleColors import green
from scripts.Constants import (
    TRADE_EVENT_FAILURE_CRIT_BOUND,
    TRADE_EVENT_FAILURE_SIMPLE_BOUND,
    TRADE_EVENT_SUCCESS_SIMPLE_BOUND,
    TRADE_EVENT_SUCCESS_CRIT_BOUND,
    WEEK_TAX,
    YOU_STRING
)
from scripts.visual.Converter import POSTFIXES, COEFFS
from scripts.visual.SmoothPrint import smoothPrint
from scripts.visual.Methods import showStory, bcolors
from texts.events import TradeTexts


def TradeEvent(w):
  return EventFunc(
      w,
      requestBet,
      TradeTexts,
      __calcDice__,
      TRADE_EVENT_FAILURE_CRIT_BOUND,
      TRADE_EVENT_FAILURE_SIMPLE_BOUND,
      TRADE_EVENT_SUCCESS_SIMPLE_BOUND,
      TRADE_EVENT_SUCCESS_CRIT_BOUND,
      lambda w: (w._replace(g=w.g._replace(
          wealth=w.g.wealth - w.yourBet,
          actionPoints=w.g.actionPoints - 1
      )), None),
      lambda w: (w._replace(g=w.g._replace(
          wealth=w.g.wealth + WEEK_TAX / 7,
          actionPoints=w.g.actionPoints - 1
      )), None),
      lambda w: (w._replace(g=w.g._replace(
          wealth=w.g.wealth + w.yourBet * (1 / 3),
          actionPoints=w.g.actionPoints - 1
      )), None),
      lambda w: (w._replace(g=w.g._replace(
          wealth=w.g.wealth + w.yourBet * (3 / 3),
          actionPoints=w.g.actionPoints - 1
      )), None),
      showChangedPropsAfterAll=True
  )


def requestBet(w):
  def req():
    smoothPrint('Your wealth: {}{}{}'.format(
        bcolors.BOLD,
        round(w.g.wealth * COEFFS['wealth']),
        bcolors.ENDC,
    ))
    return input('Place you bet: ')

  while True:
    value = req()
    if value.isdigit() and int(value) / COEFFS['wealth'] <= w.g.wealth:
      showStory(
          '''
            Your bet accepted
            Now you're trying to have a profit
      '''
      )
      return w._replace(yourBet=int(value) / COEFFS['wealth'])

    # if bet is invalid
    showStory(TradeTexts.REPLACE_BET_REQUEST)


def __calcDice__(w):
  dd = (20, 1)
  dice = rollDice(*dd)
  d = dice + w.g.tradingLevel
  showRollResult(
      YOU_STRING,
      '{} + {}'.format(
          dice,
          w.g.tradingLevel
      ),
      'd{}x{} + tradingLevel'.format(
          green(dd[0]),
          green(dd[1]),
      ),
      d,
      TRADE_EVENT_FAILURE_CRIT_BOUND,
      TRADE_EVENT_FAILURE_SIMPLE_BOUND,
      TRADE_EVENT_SUCCESS_SIMPLE_BOUND,
      TRADE_EVENT_SUCCESS_CRIT_BOUND,
  )
  return d
