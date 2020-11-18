alphabet = "abcdefghijklmnopqrstuvwxyz"
def count_code(str):
  x = "code"
  return sum([str.count(x.replace("d", y)) for y in alphabet])
