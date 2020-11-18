def front_back(stra):
  if stra == "":
    return ""
  ls = list(stra)
  ls[0], ls[-1] = ls[-1], ls[0]
  return "".join(ls)
