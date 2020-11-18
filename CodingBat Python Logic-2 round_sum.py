def round10(num):
  return round(num, -1)
def round_sum(a, b, c):
  return sum([int(round10(x)) for x in [a,b,c]])
