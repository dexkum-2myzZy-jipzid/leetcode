class Solution {
    public int minAddToMakeValid(String s) {
        int right = 0;
        int left = 0;
        for(char c : s.toCharArray()){
            if(c == '('){
                right++;
            }
            if(c == ')'){
                if(right == 0){
                    left++;
                }else{
                    right--;
                }
            }
        }
        return right+left;
    }
}