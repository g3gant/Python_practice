def twoSum(nums, target):
    stack = {}
    for i,v in enumerate(nums):
        diff = target - v

        if stack.get(diff)==None:
            stack[v] = i
        else:
            return (i,stack[diff])

nums = [2,7,11,15]
tar = 9

print(twoSum(nums,tar))