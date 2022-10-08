class Solution:
    def minPartitions(self, n: str) -> int:
        # we need at least k deci-binary if k is the maximum digit in a number
        nums = 0
        for character in n:
            if int(character) > nums:
                nums = int(character)
        return nums