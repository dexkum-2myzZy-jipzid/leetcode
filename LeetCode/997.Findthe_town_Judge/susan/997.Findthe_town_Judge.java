class Solution {
    public int findJudge(int n, int[][] trust) {

        int[] member = new int[n+1];

        for(int i = 0; i< trust.length; i++){
             member[trust[i][0]]--;
             member[trust[i][1]]++;
        }

        for(int j = 1; j <= n; j++){
            if(member[j] == n-1){
                return j;
            }
        }

        return -1;
    }
}
