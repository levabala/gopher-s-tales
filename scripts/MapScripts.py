from scripts.areas.EmptyArea import EmptyArea


def stringMapToAreas(m, areas):
  areasDict = {a()['symbol']: a for a in areas}

  lines = [l.strip() for l in m.split('\n') if len(l) > 0]
  areas = []
  for line in lines:
    arr = list(line)
    arr.pop()
    arr.reverse()
    arr.pop()
    arr.reverse()

    mapLine = ''.join(arr)
    areasInLine = [areasDict[a]() if a in areasDict else EmptyArea() for a in mapLine]
    areas.append(areasInLine)
  return areas
