from classes.Gopher import Gopher


def runGameCycle(exitCommand='exit'):
  gopher = Gopher(name="Jackob")

  command = 'none'
  day = 0
  while command != exitCommand:
    # increment day
    day += 1
    print('\n--- Day {} ---'.format(day))

    # check for dying
    died = gopher.maybeIsDied()
    if died:
      print('Oh fuck. You\'ve just died, gopher. See u later ;)')
      break

    # handle&perform command
    passed = False
    while not passed:
      try:
        command = raw_input('Enter command:\n')

        runCommand(command, gopher)
        passed = True
      except Exception as e:
        print(e)
        print()

    # night
    gopher.sleep()


def runCommand(cmd, targetGopher):
  commandsMap = {
      'dig': (lambda: targetGopher.dig()),
      'fight': (lambda: targetGopher.fight()),
      'eat': (lambda: targetGopher.eat()),
      'trade': (lambda: targetGopher.trade()),
      'spy': (lambda: targetGopher.spy()),
      'none': (lambda: None),
      '': (lambda: None),
  }

  cmd = cmd.lower()

  if not cmd in commandsMap:
    raise Exception('no such command!')

  commandsMap[cmd]()
