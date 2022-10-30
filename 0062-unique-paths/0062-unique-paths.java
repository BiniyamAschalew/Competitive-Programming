class Solution {
    public int uniquePaths(int m, int n) {
        int[][] sMatrix = new int[m][n];
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++ ){
                if (i == 0 || j == 0) sMatrix[i][j] = 1;
                else sMatrix[i][j] = sMatrix[i][j-1] + sMatrix[i-1][j];
            }
        } return sMatrix[m-1][n-1];
        
    }
}