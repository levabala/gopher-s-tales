from scripts.EventPipe import EventPipe

from scripts.events.performable.PurgeEvent import PurgeEvent


def MonstersArea(): return {
    'purge': lambda w: EventPipe(w, PurgeEvent),
    'monsters count': 0,
}
