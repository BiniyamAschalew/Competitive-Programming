class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]
        backward = [1]
        output = []
        for i in range(len(nums) - 1):
            forward.append(forward[i] * nums[i])
            j = len(nums) - (i + 1)
            backward.insert(0, backward[0] * nums[j] )
        for i in range(len(forward)):
            output.append(forward[i] * backward[i])
        return output