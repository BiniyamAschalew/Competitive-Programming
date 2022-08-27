class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum, max_sum = 0, nums[0]
        for i in range(len(nums)):
            if current_sum < 0:
                current_sum = nums[i]
            else:
                current_sum += nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum