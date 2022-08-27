class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m_p , c_p  = float("-inf"), 1
        for i in range(len(nums)):
            c_p = c_p * nums[i]
            m_p = max(m_p, c_p)
            if nums[i] == 0:
                c_p = 1
        c_p = 1
        for i in range(len(nums))[::-1]:
            c_p = c_p * nums[i]
            m_p = max(m_p, c_p)
            if nums[i] == 0:
                c_p = 1
        return m_p
            