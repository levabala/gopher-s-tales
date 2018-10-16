class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


class GopherProp:
  def __init__(self, name, value, nightChangeFunc, isFatalCondition):
    self.name = name
    self.value = value
    self.nightChangeFunc = nightChangeFunc
    self.isFatalCondition = isFatalCondition

  def add(self, delta):
    self.changeValue(delta=delta)

  def changeValue(self, newValue=None, delta=None, doPrint=True):
    if newValue is None and delta is None:
      raise Exception('too little params passed!')

    delta = delta if not delta is None else newValue - self.value
    self.value += delta
    self.value = round(min(self.value, 1), 2)
    if doPrint:
      print('>> {} changed to {} ({}{})'.format(
          self.name,
          self.formatValueColored(),
          '+' if delta >= 0 else '',
          delta)
      )

  def nightPassed(self, gopher):
    self.changeValue(delta=self.nightChangeFunc(gopher), doPrint=False)
    return self.checkIfFatal()

  def checkIfFatal(self):
    return self.isFatalCondition(self.value)

  def __str__(self):
    return "{}: {}".format(self.name, self.formatValueColored())

  def formatValueColored(self):
    start = ''
    if self.value < 0.2:
      start = bcolors.FAIL
    elif self.value < 0.5:
      start = bcolors.WARNING
    elif self.value < 0.7:
      start = bcolors.OKBLUE
    else:
      start = bcolors.OKGREEN

    return "{}{}{}".format(start, self.value, bcolors.ENDC)
