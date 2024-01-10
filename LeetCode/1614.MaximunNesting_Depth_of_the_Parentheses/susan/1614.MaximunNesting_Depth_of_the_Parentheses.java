class Solution {
    public int maxDepth(String s) {
        int res = 0;
        int count = 0;
        for(char c : s.toCharArray()){
            if(c == '('){
                count++;
            }
            if(c == ')'){
                count--;
            }

            res = Math.max(res,count);
        }

        return res;
    }
}