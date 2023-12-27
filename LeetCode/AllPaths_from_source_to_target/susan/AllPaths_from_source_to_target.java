class Solution {
    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<Integer> path = new ArrayList<>();
        traverse(graph, 0, path);
        return res;
    }

    void traverse(int[][] graph, int s, List<Integer> path){

        path.addLast(s);

        int n = graph.length;

        if( s == n-1){
            res.add(new ArrayList<>(path));
        }

        for(int neight : graph[s]){
            traverse(graph, neight, path);
        }

        path.removeLast();
    }
}