def singleNumber(nums):
  result = 0
  for n in nums:
    result ^= n
  return result


print(singleNumber([4, 1, 4, 2, 2]))