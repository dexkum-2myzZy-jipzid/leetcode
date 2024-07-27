class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        // queries[j] = [uj, vj]， course uj is a prerequisite of course vj or not
        // build matrix to store prerequisite

        // create graph
        List<List<Integer>> graph = new ArrayList<>();
        int[] indegree = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        // [0, 1], 0->1
        for (int[] p : prerequisites) {
            int from = p[0], to = p[1];
            graph.get(from).add(to);
            indegree[to] += 1;
        }

        boolean[][] matrix = new boolean[numCourses][numCourses];
        Set<Integer> visited = new HashSet<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                dfs(visited, new HashSet<>(), i, graph, matrix);
            }
        }

        List<Boolean> result = new ArrayList<>();
        for (int[] q : queries) {
            int from = q[0], to = q[1];
            result.add(matrix[from][to]);
        }

        return result;
    }

    private void dfs(Set<Integer> visited, Set<Integer> stack, int cur, List<List<Integer>> graph, boolean[][] matrix) {
        visited.add(cur);
        stack.add(cur);
        for (int nei : graph.get(cur)) {
            matrix[cur][nei] = true;
            if (!visited.contains(nei) && !stack.contains(nei)) {
                dfs(visited, stack, nei, graph, matrix);
            }
            // a -> b -> c, and a is also a prerequisite for c
            for (int i = 0; i < matrix.length; i++) {
                if (matrix[nei][i]) {
                    matrix[cur][i] = true;
                }
            }
        }
        stack.remove(cur);
    }
}