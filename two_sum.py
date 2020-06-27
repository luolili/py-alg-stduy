from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key num,v:i
        map = {}
        for index, num in enumerate(nums):
            map[num] = index
        for i, n in enumerate(nums):
            j = map.get(target - n)
            if j is not None and i != j:
                return [i, j]

    # time:o:n;space:o:n
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # key num,v:i
        map = {}
        for index, num in enumerate(nums):
            other = target - num
            if other in map:
                return [map.get(other), index]
            else:
                item = {num: index}
                map.update(item)

    # 暴力法
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        count = len(nums)
        for i in range(count):
            for j in range(i + 1, count):
                if target - nums[i] == nums[j]:
                    return [i, j]


if __name__ == '__main__':
    t = TwoSum()
    nums = [1, 2, 3, 4, 5, 6]
    res = t.twoSum(nums, 9)
    res2 = t.twoSum2(nums, 9)
    print(res, res2)
