def sum67(nums):
  f = False
  for x in range(len(nums)):
    if f:
      if nums[x] == 7:
        f = False
      nums[x] = 0
    if nums[x] == 6:
      nums[x] = 0
      f = True
  return sum(nums)
    