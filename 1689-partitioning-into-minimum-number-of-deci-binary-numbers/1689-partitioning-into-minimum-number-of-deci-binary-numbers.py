class Solution:
    def minPartitions(self, n: str) -> int:
        # we need at least k deci-binary if k is the maximum digit in a number 
        return int(max(list(n)))
