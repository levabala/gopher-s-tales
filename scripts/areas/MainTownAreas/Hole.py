from scripts.areas.RootArea import RootArea
from scripts.EventPipe import EventPipe

# possible events
from scripts.events.performable.DigEvent import DigEvent


def HoleArea(): return {
    'area name': 'Hole',
    'symbol': 'H',
    'dig': lambda w: EventPipe(w, DigEvent),
    'move cost': 0,
    **RootArea()
}
