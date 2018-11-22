from scripts.EventPipe import EventPipe

from scripts.events.performable.PurgeEvent import PurgeEvent


def MonstersArea(): return {
    'fight': lambda w: EventPipe(w, PurgeEvent),
    'monsters count': 0,
    # 'search': checkForMonsters,
}
