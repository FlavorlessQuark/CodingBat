def array123(nums):
  return True if "".join(map(str, nums)).find("123") != -1 else False
