class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int len = cost.length;
        if (len < 2) return 0;
        int[] array = new int[len];
        for (int i = 0; i < len; i++){
            if (i < 2) array[i] = cost[i];
            else {
                array[i] = cost[i] + Math.min(array[i-1], array[i-2]);
            }
        }
        return Math.min(array[len-1], array[len-2]);
    }
}