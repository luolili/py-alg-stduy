class FindRepeatNum:
    # 超时
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        nLen = len(nums)
        while i < nLen:
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]

        return -1

    def f2(self, nums: [int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                return n
            else:
                s.add(n)
