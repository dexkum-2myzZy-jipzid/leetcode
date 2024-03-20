class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < prerequisites.length; i++) {
            int[] arr = prerequisites[i];
            int a = arr[0], b = arr[1];
            List<Integer> list = graph.getOrDefault(b, new ArrayList<Integer>());
            list.add(a);
            graph.put(b, list);
        }

        for (Integer key : graph.keySet()) {
            if (!dfs(graph, set, key)) {
                return false;
            }
        }
        return true;
    }

    private boolean dfs(Map<Integer, List<Integer>> graph, Set<Integer> set, Integer next) {
        if (set.contains(next)) {
            return false;
        }

        if (!graph.containsKey(next)) {
            return true;
        }

        List<Integer> list = graph.get(next);
        if (list == null) {
            return true;
        } else {
            for (Integer val : list) {
                set.add(next);
                if (!dfs(graph, set, val)) {
                    set.remove(next);
                    return false;
                }
                set.remove(next);
            }
            graph.put(next, new ArrayList<Integer>());
            return true;
        }
    }

}

// Topological sort
class Solution {
    // [1, 0]: 0 -> 1
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        // create directed graph
        List<List<Integer>> graph = new ArrayList<>(numCourses);
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        // store indegree
        for (int[] arr : prerequisites) {
            graph.get(arr[1]).add(arr[0]);
            indegree[arr[0]] += 1;
        }

        // find 0 indegree node
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0)
                queue.offer(i);
        }

        // topological sort
        int visited = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            visited += 1;

            for (int neighbor : graph.get(node)) {
                indegree[neighbor] -= 1;
                if (indegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        return visited == numCourses;
    }
}