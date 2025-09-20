class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        int size = equations.size();

        UnionFind uf = new UnionFind(2 * size);
        HashMap<String, Integer> hm = new HashMap<>(2 * size);
        int idx = 0;
        int index = 0;
        for(List<String> eq: equations){
            String v1 = eq.get(0);
            String v2 = eq.get(1);

            if(!hm.containsKey(v1)){
                hm.put(v1, idx);
                idx += 1;
            }

            if(!hm.containsKey(v2)){
                hm.put(v2, idx);
                idx += 1;
            }

            uf.union(hm.get(v1), hm.get(v2), values[index]);
            index += 1;
        }

        int s = queries.size();
        double[] res = new double[s];
        for(int i = 0; i < s; i++){
            List<String> q = queries.get(i);
            String v1 = q.get(0);
            String v2 = q.get(1);

            Integer j = hm.get(v1);
            Integer k = hm.get(v2);

            if(j == null || k == null){
                res[i] = -1.0d;
            }else{
                res[i] = uf.isConnected(j, k);
            }
        }

        return res;
    }

    private class UnionFind{

        private int[] parents;
        private double[] weights;

        public UnionFind(int size){
            this.parents = new int[size];
            this.weights = new double[size];

            for(int i = 0; i < size; i++){
                parents[i] = i;
                weights[i] = 1.0d;
            }
        }

        // find root
        public int find(int x){
            if(x != parents[x]){
                int origin = parents[x];
                parents[x] = find(parents[x]);
                weights[x] *= weights[origin];
            }
            return parents[x];
        }

        public void union(int x, int y, double value){
            int rootX = find(x);
            int rootY = find(y);
            if(rootX == rootY){
                return;
            }

            parents[rootX] = rootY;
            weights[rootX] = weights[y] * value / weights[x];
        }

        public double isConnected(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if(rootX == rootY){
                return weights[x] / weights[y];
            }else{
                return -1.0d;
            }
        }

    }
}