class Solution {
    public int rob(int[] nums) {
        int len = nums.length;
        int[] value = new int[len];
        for (int i = 0; i < len; i++){
            if (i == 0) {value[i] = nums[0];}
            else if (i == 1) {value[i] = Math.max(nums[0], nums[1]);}
            else{
                value[i] = Math.max((value[i-2] + nums[i]), value[i - 1]);
            }
        } return value[len - 1];
        
    }
}