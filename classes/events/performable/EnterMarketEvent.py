from toolz.functoolz import pipe
from classes.ConsoleColors import bcolors
from classes.Event import __EventTrivialFunc__
from classes.GopherVisual import showStory, smoothPrint
from texts.events import EnterMarketTexts
from classes.events.TradeEvent import TradeEvent
from classes.Converter import POSTFIXES, COEFFS


def EnterMarketEvent(rt):
  return __EventTrivialFunc__(
      rt,
      EnterMarketTexts,
      lambda rt: pipe(rt, __requestBet__, TradeEvent)
  )


def __requestBet__(rt):
  def req():
    smoothPrint('Your wealth: {}{}{}'.format(
        bcolors.BOLD,
        round(rt.g.wealth * COEFFS['wealth']),
        bcolors.ENDC,
    ))
    return int(input('Place you bet: '))

  while True:
    value = req()
    if type(value) is int:
      return rt._replace(
          w=rt.w._replace(yourBet=min(value / COEFFS['wealth'], rt.g.wealth))
      )

    # if bet is invalid
    showStory(EnterMarketTexts.REPLACE_BET_REQUEST)
