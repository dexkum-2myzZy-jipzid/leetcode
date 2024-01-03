class Solution {
    public boolean equationsPossible(String[] equations) {
        int n = equations.length;
        UF uf = new UF(26);
        int count = 0;
        for(String equation: equations){
            int i = equation.charAt(0)-'a';
            int j = equation.charAt(3)-'a';
            char operation = equation.charAt(1);
            if( operation == '='){
                if(uf.checkUnion(i,j)){
                     continue;
                }else{
                    uf.union(i,j);
                }
            }
        }

        for(String equation: equations){
            int i = equation.charAt(0)-'a';
            int j = equation.charAt(3)-'a';
            char operation = equation.charAt(1);
            if( operation == '!'){
                if(uf.checkUnion(i,j)){
                     return false;
                }
            }
        }

        return true;
    }
}

class UF{
    int[] parent;
    public UF(int n){
        parent = new int[n];
        for(int i = 0; i< n; i++){
            parent[i] = i;
        }
    }

    public int find(int x){
        if(parent[x] != x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public void union(int x, int y){
        int rootX = find(x);
        int rootY = find(y);
        if(rootX == rootY){
            return;
        }else{
            parent[rootX] = rootY;
        }
    }

    public boolean checkUnion(int x , int y){
        int rootX = find(x);
        int rootY = find(y);
        return rootX == rootY;
    }

   
}