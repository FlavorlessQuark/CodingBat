def pos_neg(a, b, negative):
  return a &lt; 0 and b &lt; 0 if negative else ((a &lt; 0 and b &gt; 0) or (a &gt; 0 and b &lt; 0))
