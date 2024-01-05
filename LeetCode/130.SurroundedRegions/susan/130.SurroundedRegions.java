class Solution {
    public void solve(char[][] board) {
        if(board.length == 0) return;

        int m = board.length;
        int n = board[0].length;

        UF uf = new UF(m*n + 1);
        int dummy = m*n;

        for(int i = 0; i< m; i++){
            if(board[i][0] == 'O'){
                uf.union(i*n,dummy);
            }
            if(board[i][n-1] == 'O'){
                uf.union(i*n+n-1,dummy);
            }
        }

        for(int j = 0; j< n ; j++){
            if(board[0][j] == 'O'){
                uf.union(j,dummy);
            }
            if(board[m-1][j] == 'O'){
                uf.union(n*(m-1)+j,dummy);
            }
        }

        int[][] d = new int[][]{{1,0},{0,1},{0,-1},{-1,0}};
        for(int i = 1; i< m-1; i++){
            for(int j = 1; j< n-1; j++){
                if(board[i][j] == 'O'){
                    for(int k = 0; k < 4; k++){
                        int x = i + d[k][0];
                        int y = j + d[k][1];
                        if(board[x][y] == 'O'){
                            uf.union(x*n+y, i*n+j);
                        }
                    }
                }
            }
        }

        for(int i = 1; i< m-1; i++){
            for(int j = 1; j< n-1; j++){
                if(!uf.connected(dummy,i *n + j)){
                    board[i][j] = 'X';
                }
            }
        }
    }
}

class UF{
    int[] parent;
    int[] size;

    public UF(int n){
        parent = new int[n];
        size = new int[n];
        for(int i = 0; i< n; i++){
            parent[i] = i;
            size[i] = 1;
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
        }

        if (size[rootX] > size[rootY]) {
            parent[rootX] = rootY;
            size[rootX] += size[rootY];
        } else {
            parent[rootX] = rootY;
            size[rootX] += size[rootY];
        }
    }

    public boolean connected(int x, int y){
        return find(x) == find(y);
    }
}