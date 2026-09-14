class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = dict()
        indices = []
        for i in range(len(nums)):
            if nums[i] in diffs:
                indices = [diffs[nums[i]], i]
                break
            diffs[target - nums[i]] = i
        return indices