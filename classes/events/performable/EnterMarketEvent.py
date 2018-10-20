from toolz.functoolz import pipe
from classes.Event import __EventTrivialFunc__
from classes.GopherVisual import showStory
from texts.events import EnterMarketTexts
from classes.events.TradeEvent import TradeEvent


def EnterMarketEvent(rt):
  return __EventTrivialFunc__(
      rt,
      EnterMarketTexts,
      lambda rt: pipe(rt, __requestBet__, TradeEvent)
  )


def __requestBet__(rt):
  def req():
    return int(input('Place you bet: '))

  while True:
    value = req()
    if type(value) is int:
      return rt._replace(
          w=rt.w._replace(yourBet=value)
      )

    # if bet is invalid
    showStory(EnterMarketTexts.REPLACE_BET_REQUEST)
