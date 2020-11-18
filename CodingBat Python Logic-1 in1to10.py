def in1to10(n, outside_mode):
  if outside_mode:
    return True if n &lt;= 1 or n &gt;= 10  else False
  return True if 1 &lt;= n &lt;= 10 else False