# 删除数组里面重复的元素

def removeDulplicates(nums):
    last_index = len(nums) - 1
    for i in range(last_index, 0, -1):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
    return len(nums)
