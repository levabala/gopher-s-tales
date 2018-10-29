from scripts.EventPipe import EventPipe

# possible events
from scripts.events.performable.MoveNorthEvent import MoveNorthEvent
from scripts.events.performable.MoveEastEvent import MoveEastEvent
from scripts.events.performable.MoveSouthEvent import MoveSouthEvent
from scripts.events.performable.MoveWestEvent import MoveWestEvent
from scripts.events.performable.LeaveRegionEvent import LeaveRegionEvent


def ConnectedArea(): return {
    'go north': lambda w: EventPipe(w, MoveNorthEvent),
    'go east': lambda w: EventPipe(w, MoveEastEvent),
    'go south': lambda w: EventPipe(w, MoveSouthEvent),
    'go west': lambda w: EventPipe(w, MoveWestEvent),
    'die': lambda w: w._replace(g=w.g._replace(alive=False)),
    'leave region': lambda w: EventPipe(w, LeaveRegionEvent),
}
