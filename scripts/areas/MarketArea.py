from scripts.areas.RootArea import RootArea
from scripts.EventPipe import EventPipe

# possible events
from scripts.events.performable.TradeEvent import TradeEvent
from scripts.events.performable.BuyAndEatEvent import BuyAndEatEvent


def MarketArea(): return {
    'area name': 'Market',
    'trade': lambda w: EventPipe(w, TradeEvent),
    'buyeat': lambda w: EventPipe(w, BuyAndEatEvent),
    **RootArea()
}
