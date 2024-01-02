class Solution {
    int[][] dirts = {{0,-1},{0,1},{-1,0},{1,0}};
    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        UF uf = new UF(m*n);
        boolean[][] visited = new boolean[m][n];
        List<Integer> res = new ArrayList<>();
        int count = 0;
        for(int[] position : positions){
            if(visited[position[0]][position[1]]){
                res.add(count);
                continue;
            }

            visited[position[0]][position[1]]= true;
            count++;
            for(int[] dirt : dirts){
                int x = position[0]+dirt[0];
                int y = position[1]+dirt[1];

                if( x <0 || x >= m || y <0 || y >= n || visited[x][y] == false) continue;

                int component1 = uf.find(position[0]*n + position[1]);
                int component2 = uf.find(x*n + y);

                if(component1 != component2){
                    uf.union(component1, component2);
                    count--;
                }
            }
            res.add(count);

        }

        return res;
    }
}

class UF {
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