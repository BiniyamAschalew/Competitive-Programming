class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_store = {}
        for i in range(len(nums)):
            if nums[i] in target_store:
                return [target_store[nums[i]], i]
            else:
                target_store[target - nums[i]] = i