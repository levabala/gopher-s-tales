class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def bold(string):
  return '{}{}{}'.format(bcolors.BOLD, string, bcolors.ENDC)


def green(string):
  return '{}{}{}'.format(bcolors.OKGREEN, string, bcolors.ENDC)


def blue(string):
  return '{}{}{}'.format(bcolors.OKBLUE, string, bcolors.ENDC)
