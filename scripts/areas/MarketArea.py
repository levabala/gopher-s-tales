from scripts.areas.ConnectedArea import ConnectedArea
from scripts.EventPipe import EventPipe

# possible events
from scripts.events.performable.TradeEvent import TradeEvent


def MarketArea(): return {
    'area name': 'Market',
    'trade': lambda w: EventPipe(w, TradeEvent),
    **ConnectedArea()
}
