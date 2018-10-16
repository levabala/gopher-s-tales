from collections import namedtuple
from classes.GopherProp import GopherProp


class Gopher:
  def __init__(self, name='Gopher withot name', hp=1, power=0.5, authority=0.5, satiety=0.5, holeDeep=0.5):
    self.name = name
    self.hpProp = GopherProp(
        name='hp',
        value=hp,
        nightChangeFunc=lambda gopher: 0.1,
        isFatalCondition=lambda value: value <= 0
    )
    self.powerProp = GopherProp(
        name='power',
        value=power,
        nightChangeFunc=lambda gopher: (1 - gopher.powerProp.value) * 0.1,
        isFatalCondition=lambda value: False
    )
    self.authorityProp = GopherProp(
        name='authority',
        value=authority,
        nightChangeFunc=lambda gopher: -0.01,
        isFatalCondition=lambda value: False
    )
    self.satietyProp = GopherProp(
        name='satiety',
        value=satiety,
        nightChangeFunc=lambda gopher: -0.1,
        isFatalCondition=lambda value: value <= 0
    )
    self.holeDeepProp = GopherProp(
        name='holeDeep',
        value=holeDeep,
        nightChangeFunc=lambda gopher: -0.03,
        isFatalCondition=lambda value: value <= 0
    )

    self.props = [
        self.hpProp, self.powerProp,
        self.authorityProp, self.satietyProp, self.holeDeepProp
    ]

  def dig(self):
    self.holeDeepProp.add(0.1)

  def fight(self):
    print('here we are doint awesome fighting')

  def eat(self):
    self.satietyProp.add(0.4)

  def trade(self):
    print('performing trading...')

  def spy(self):
    print('I AM A SPYY!)0!!')

  def sleep(self):
    print('\nNow {}\'s props are:'.format(self.name))
    for prop in self.props:
      lastValue = prop.value
      prop.nightPassed(self)
      delta = round(prop.value - lastValue, 2)
      print("  {} ({}{})".format(prop, '+' if delta >= 0 else '', delta))

  def maybeIsDied(self):
    for prop in self.props:
      if prop.checkIfFatal():
        return True
    return False
