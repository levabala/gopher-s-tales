from collections import namedtuple

World = namedtuple('World', [
    'gopherAfterNight',
    'weekday',
    'totalDays',
    'yourBet',
])

# set default values
World.__new__.__defaults__ = (None,) * len(World._fields)


def defaultWorld():
  return World(
      gopherAfterNight=None,
      totalDays=0,
      yourBet=0,
  )
