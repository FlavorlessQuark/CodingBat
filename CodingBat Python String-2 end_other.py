def end_other(a, b):
  return True if a.lower().endswith(b.lower()) or b.lower().endswith(a.lower()) else False
