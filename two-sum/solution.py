class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dict:
                j = dict[target - nums[i]]
                return [i, j]
            else:
                dict[nums[i]] = i