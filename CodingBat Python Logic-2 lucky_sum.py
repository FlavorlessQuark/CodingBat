def lucky_sum(a, b, c):
  l = [a,b,c]
  c =  l.index(13) if 13 in l else 3

  return sum(l[:c])
