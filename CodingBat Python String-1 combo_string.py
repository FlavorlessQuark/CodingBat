def combo_string(a, b):
  return a + b + a if len(a) &lt; len(b) else b + a + b
