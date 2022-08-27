class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1=min1=ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                max1,min1=min1,max1
            max1=max(nums[i],max1*nums[i])
            min1=min(nums[i],min1*nums[i])
            ans=max(ans,max1)
        return ans