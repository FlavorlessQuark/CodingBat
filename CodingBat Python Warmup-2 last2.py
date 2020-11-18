def last2(str):
  if  str == "":
    return 0
  return sum(1 for i, _ in enumerate(str) if str.startswith(str[-2:], i)) - 1