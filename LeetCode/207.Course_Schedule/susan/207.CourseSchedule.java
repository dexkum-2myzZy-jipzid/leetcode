class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = buildGraph(numCourses,prerequisites);

        int[] indegree = new int[numCourses];

        for(int[] edge : prerequisites){
            indegree[edge[0]]++;
        }

        Queue<Integer> q = new LinkedList<>();

        int count = 0;

        for(int i = 0; i< numCourses; i++){
            if(indegree[i] == 0){
                q.offer(i);
            }
        }

        while(!q.isEmpty()){
            int cur = q.poll();
            count++;
            for(int neight : graph[cur]){
                indegree[neight]--;
                if(indegree[neight] == 0){
                    q.offer(neight);
                }
            }
        }

        if(count != numCourses){
            return false;
        }

        return true;
    }

    public List<Integer>[] buildGraph(int numCourses, int[][] prerequisition){
        List<Integer>[] graph = new LinkedList[numCourses];

        for(int i = 0; i< numCourses; i++){
             graph[i] = new LinkedList<>();
        }

        for(int[] edge : prerequisition){
            int from = edge[1];
            int to = edge[0];
            graph[from].add(to);
        }

        return graph;
    }

}