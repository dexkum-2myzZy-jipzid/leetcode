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

// DFS
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // create graph
        Map<Integer, List<Integer>> adjList = new HashMap<>();
        Set<Integer> visited = new HashSet<>();
        boolean[] sources = new boolean[numCourses];
        Arrays.fill(sources, true);

        for (int i = 0; i < numCourses; i++) {
            adjList.put(i, new ArrayList<>());
        }

        // add node and find source
        for (int[] p : prerequisites) {
            int pre = p[1], post = p[0];
            adjList.get(pre).add(post);
            sources[post] = false;
        }

        // bfs
        List<Integer> result = new ArrayList<>(numCourses);
        for (int i = 0; i < numCourses; i++) {
            if (sources[i]) {
                boolean ok = dfs(i, adjList, visited, new HashSet<Integer>(), result);
                if (!ok) {
                    return new int[0];
                }
            }
        }

        // have cycle
        if (result.size() < numCourses) {
            return new int[0];
        }

        // Reverse the solution and put it into an array.
        int[] ans = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            ans[i] = result.get(numCourses - 1 - i);
        }
        return ans;
    }

    private boolean dfs(int i, Map<Integer, List<Integer>> adjList, Set<Integer> visited, Set<Integer> stack,
            List<Integer> result) {
        visited.add(i);
        stack.add(i);
        for (int nei : adjList.get(i)) {
            if (visited.contains(nei)) {
                if (stack.contains(nei)) {
                    return false;
                }
            } else {
                boolean ok = dfs(nei, adjList, visited, stack, result);
                if (!ok) {
                    return false;
                }
            }
        }
        stack.remove(i);
        result.add(i);
        return true;
    }

}