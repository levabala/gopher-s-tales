import os
import sys
import readline
import glob


class TabCompleter(object):
  def createListCompleter(self, ll):
    def listCompleter(text, state):
      line = readline.get_line_buffer()

      if not line:
        return [c + " " for c in ll][state]

      else:
        return [c + " " for c in ll if c.startswith(line)][state]

    self.listCompleter = listCompleter


def requestCompletableInputStrict(options, requestString='', wrongInputString='Invalid input'):
  name = requestCompletableInput(options=options, requestString=requestString)

  while not name in options:
    print(wrongInputString)
    name = requestCompletableInput(options=options, requestString=requestString)

  return name


def requestCompletableInput(options, requestString=''):
  t = TabCompleter()
  t.createListCompleter(options)

  readline.set_completer_delims('\t')
  readline.parse_and_bind("tab: complete")

  readline.set_completer(t.listCompleter)

  ans = input(requestString)
  print(ans)
  print()

  return ans.strip()
