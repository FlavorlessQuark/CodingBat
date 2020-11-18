def lone_sum(a, b, c):
  return sum([x for x in[a,b,c] if [a,b,c].count(x) &lt; 2])
