from scripts.areas.ConnectedArea import ConnectedArea
from scripts.EventPipe import EventPipe

# possible events
from scripts.events.performable.DigEvent import DigEvent


def HoleArea(): return {
    'area name': 'Hole',
    'dig': lambda w: EventPipe(w, DigEvent),
    **ConnectedArea()
}
