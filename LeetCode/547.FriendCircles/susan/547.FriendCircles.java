class Solution {
    public int findCircleNum(int[][] isConnected) {
        int m = isConnected.length;
        UF uf = new UF(m);
        for(int i = 0; i< m ; i++){
            for(int j = 0; j< m ; j++){
                if(isConnected[i][j] == 1){
                    uf.union(i,j);
                }
            }
        }
        int res = 0;
        for(int i = 0; i< m; i++){
            if(uf.find(i) == i){
                res++;
            }
        }

        return res;
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

    public void union(int x , int y){
        parent[find(x)] = find(y);
    }
}