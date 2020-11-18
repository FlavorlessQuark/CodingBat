def close_far(a, b, c):
  close = b if abs(b - a) &lt;= 1 else c if abs(c - a) &lt;= 1 else - 1
  far = b if close == c else c
  return abs(close - a) &lt;= 1 and abs(far - a) &gt;= 2 and abs(far - close) &gt;= 2