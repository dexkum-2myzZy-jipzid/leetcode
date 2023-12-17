class Solution {
    public String simplifyPath(String path) {
        String[] paths = path.split("/");
        Stack<String> s = new Stack<>();
        for(String p : paths){
            if(p.isEmpty() || p.equals(".")){
                 continue;
            }
            if(p.equals("..")){
                if(!s.isEmpty()){
                    s.pop();
                } 
                continue;
            }
            s.push(p);
        }
        String res = "";

        while(!s.isEmpty()){

           res = "/" + s.pop() + res;
        }

        return res.isEmpty() ? "/":res;
    }
}