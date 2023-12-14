class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new LinkedList<>();
        StringBuilder sb = new StringBuilder();
        int left = n;
        int right = n;
        dfs(left,right,sb,res);
        return res;
    }

    public void dfs(int left, int right, StringBuilder sb, List<String> res){
        if(left < 0 || right < 0){
            return;
        }

        if(left > right){
            return;
        }

        if(left ==0 && right == 0){
            res.add(sb.toString());
            return;
        }

        sb.append("(");
        dfs(left-1,right,sb,res);
        sb.deleteCharAt(sb.length()-1);

        sb.append(")");
        dfs(left,right-1,sb,res);
        sb.deleteCharAt(sb.length()-1);

    }
}
