from scripts.EventPipe import EventPipe
from scripts.areas.ConnectedArea import ConnectedArea
from scripts.areas.EmptyArea import EmptyArea
from scripts.areas.ForestArea import ForestArea
from scripts.areas.RoadArea import RoadArea
from scripts.areas.MarketArea import MarketArea
from scripts.areas.HoleArea import HoleArea
from scripts.events.performable.EnterRegionEvent import EnterRegionEvent

# TODO: make area possible to return different data: events, numbers etc.


def MidTownAreas(): return {
    'area name': 'MidTown',
    'enter region': lambda w: EventPipe(w, EnterRegionEvent),
    'areas': [
        [ForestArea(), MarketArea(), ForestArea(), ForestArea()],
        [ForestArea(), HoleArea(), RoadArea(), ForestArea()],
        [ForestArea(), ForestArea(), RoadArea(), MarketArea()],
    ],
    ** ConnectedArea()
}
