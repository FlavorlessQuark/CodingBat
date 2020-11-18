def no_teen_sum(a, b, c):
  return sum([x for x in [a,b,c] if (x &lt; 13 or x &gt;19) or (x == 15 or x == 16)])  
