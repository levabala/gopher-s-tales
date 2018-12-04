from scripts.areas.RootArea import RootArea
from scripts.EventPipe import EventPipe


# possible events
from scripts.events.performable.TradeEvent import TradeEvent
from scripts.events.performable.BuyAndEatEvent import BuyAndEatEvent


def StockExchangeArea(): return {
    'area name': 'Stock Exchange',
    'symbol': '$',
    'trade': lambda w: EventPipe(w, TradeEvent),
    'buyeat': lambda w: EventPipe(w, BuyAndEatEvent),

    'move cost': 0,
    **RootArea()
}
