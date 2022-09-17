class Solution {
    public int rob(int[] nums) {
        int pre = 0, cur = 0, next = 0;
        for (int i = 0; i < nums.length; i++){
            next = Math.max(cur, pre + nums[i]);
            pre = cur;
            cur = next;
        }
        return cur;
        
        
        
        
        
    }
}