class Solution {
    public int climbStairs(int n) {
        if (n == 0) return 1;
        int first = 1, second = 1; 
        for (int i = 0; i < n-1; i++){
            second = second + first;
            int temp = first;
            first = second;
            second = temp;
            
        }
     return first;
        
    }
}