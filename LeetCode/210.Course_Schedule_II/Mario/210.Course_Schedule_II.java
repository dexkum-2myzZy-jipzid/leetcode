class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // store indegree & create graph
        int[] indegree = new int[numCourses];
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] pre : prerequisites) {
            graph.get(pre[1]).add(pre[0]);
            indegree[pre[0]] += 1;
        }

        // topological sort
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0)
                queue.offer(i);
        }

        List<Integer> res = new ArrayList<>();
        while (!queue.isEmpty()) {
            int node = queue.poll();
            res.add(node);

            for (int neighbor : graph.get(node)) {
                indegree[neighbor] -= 1;
                if (indegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        return res.size() < numCourses ? new int[] {} : res.stream().mapToInt(Integer::intValue).toArray();
    }
}