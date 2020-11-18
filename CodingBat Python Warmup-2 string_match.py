def string_match(a, b):
  return sum(1 for x in range(len(a) -1) if (a[x:x + 2] == b[x:x + 2]))
