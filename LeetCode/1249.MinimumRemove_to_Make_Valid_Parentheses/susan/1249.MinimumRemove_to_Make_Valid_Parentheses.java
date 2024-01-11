class Solution {
    public String minRemoveToMakeValid(String s) {
        Set<Integer> index = new HashSet<>();
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i< s.length(); i++){
            char c = s.charAt(i);
            if(c == '('){
                stack.push(i);
            }else if(s.charAt(i) == ')'){
                if(stack.isEmpty()){
                    index.add(i);
                }else{
                    stack.pop();
                }
            }
        }

        while(!stack.isEmpty()){
            index.add(stack.pop());
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            if(!index.contains(i)){
                sb.append(s.charAt(i));
            }
        }

        return sb.toString();
    }
}