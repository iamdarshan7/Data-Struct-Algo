def listSum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + listSum(nums[1:])    

print(listSum([1,2,3,4,5]))