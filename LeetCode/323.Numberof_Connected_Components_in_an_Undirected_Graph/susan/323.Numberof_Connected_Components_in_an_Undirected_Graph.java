class Solution {
    public int countComponents(int n, int[][] edges) {
        UF uf = new UF(n);

        for(int[] edge : edges){
            uf.union(edge[0],edge[1]);
        }
        return uf.count();
    }

    class UF{

        private int count;
        private int[] parent;

        public UF(int n){
            this.count = n;
            parent = new int[n];

            for(int i = 0; i < n ; i++){
                parent[i] = i;
            }
        }

        public void union(int p, int q){
            int rootP = find(p);
            int rootQ = find(q);

            if(rootP == rootQ){
                return;
            }

            parent[rootP] = rootQ;

            count--;
        }

        private int find(int m){
            while(parent[m]!= m){
                m = parent[m];
            }
            return m;
        }

        public int count(){
            return count;
        }

    }
}