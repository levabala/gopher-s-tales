from collections import namedtuple

MonsterState = namedtuple('MonsterState', [
    'name',
    'health',
    'evasion',
    'fightingLevel',
    'equipement',
    'holdTurnsLeft',
])


class Monster:
  def __init__(
      self,
      textModule,
      baseHealth,
      baseEvasion,
      baseFightingLevel,
      baseEquipementTypes,
  ):
    self.textModule = textModule
    self.baseHealth = baseHealth
    self.baseEvasion = baseEvasion
    self.baseFightingLevel = baseFightingLevel
    self.baseEquipementTypes = baseEquipementTypes

  def init(self):
    return MonsterState(
        health=self.baseHealth,
        evasion=self.baseEvasion,
        fightingLevel=self.baseFightingLevel,
        equipement=[equipType() for equipType in self.baseEquipementTypes],
        holdTurnsLeft=0,
        name=self.textModule.ONE_NAME,
    )

  def minDescription(self):
    return self.textModule.MIN_DESCRIPTION

  def mediumDescription(self):
    return self.textModule.MEDIUM_DESCRIPTION

  def fullDescription(self):
    return self.textModule.FULL_DESCRIPTION
