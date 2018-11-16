from scripts.areas.RootArea import RootArea
from scripts.EventPipe import EventPipe

# possible events
from scripts.events.performable.TradeEvent import TradeEvent
from scripts.events.performable.BuyAndEatEvent import BuyAndEatEvent


def ArenaArea(): return {
    'area name': 'Arena',
    'symbol': 'A',
    'fight': lambda w: w,
    'level': lambda w: w,
    'move cost': 0,
    **RootArea()
}
