def permute2Iterative(nums):
    results = []
    stack = [(nums, [])]
    while len(stack):
      nums, values = stack.pop()
      if not nums:
        results += [values]
      for i in range(len(nums)):
        stack.append((nums[:i]+nums[i+1:], values+[nums[i]]))
    return results

def _permuteHelper(nums, start=0):
    if start == len(nums) - 1:
      return [nums[:]]

    result = []
    for i in range(start, len(nums)):
      nums[start], nums[i] = nums[i], nums[start]
      result += _permuteHelper(nums, start + 1)
      nums[start], nums[i] = nums[i], nums[start]
    return result
nums = [1,2,3]

print (permute2Iterative(nums))
print (_permuteHelper(nums))