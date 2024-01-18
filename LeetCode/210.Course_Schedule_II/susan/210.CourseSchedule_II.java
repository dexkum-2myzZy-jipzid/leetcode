class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = buildGraph(numCourses,prerequisites);

        int[] indegree = new int[numCourses];

        for(int[] edge : prerequisites){
            indegree[edge[0]]++;
        }

        Queue<Integer> q = new LinkedList<>();

        for(int i = 0; i< numCourses; i++){
              if(indegree[i] == 0){
                  q.offer(i);
              }
        }

        int[] res = new int[numCourses];
        int count = 0;

        while(!q.isEmpty()){
            int cur = q.poll();
            res[count] = cur;
            count++;
            for(int edge : graph[cur]){
                indegree[edge]--;
                if(indegree[edge] == 0){
                    q.offer(edge);
                }
            }
        }

        if( count != numCourses){
            return new int[]{};
        }

        return res;
    }

    public List<Integer>[] buildGraph(int numCourses,int[][] prerequisites){
        List<Integer>[] graph = new LinkedList[numCourses];

        for(int i = 0; i< numCourses; i++){
            graph[i] = new LinkedList<>();
        }

        for(int[] edge : prerequisites){
            int from = edge[1];
            int to = edge[0];
            graph[from].add(to);
        }

        return graph;
    }
}