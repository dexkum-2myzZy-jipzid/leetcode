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

// Topological Sort - Kahn’s Algorithm
class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        // create graph using adjlist
        int n = numCourses;
        boolean[][] matrix = new boolean[n][n];
        int[] indegree = new int[n];
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] p : prerequisites) {
            int from = p[0], to = p[1];
            graph.get(from).add(to);
            indegree[to] += 1;
        }

        // topological sort
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        while (!queue.isEmpty()) {
            int cur = queue.poll();
            for (int nei : graph.get(cur)) {
                matrix[cur][nei] = true;
                for (int i = 0; i < n; i++) {
                    if (matrix[i][cur]) {
                        matrix[i][nei] = true;
                    }
                }
                indegree[nei] -= 1;
                if (indegree[nei] == 0) {
                    queue.offer(nei);
                }
            }
        }

        // iterate queries
        List<Boolean> result = new ArrayList<>();
        for (int[] q : queries) {
            result.add(matrix[q[0]][q[1]]);
        }

        return result;
    }
}

// Floyd-Warshall Algorithm
class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        int n = numCourses;
        boolean[][] matrix = new boolean[n][n];
        for (int[] p : prerequisites) {
            matrix[p[0]][p[1]] = true;
        }

        // Floyd-Warshall
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = matrix[i][j] || (matrix[i][k] && matrix[k][j]);
                }
            }
        }

        List<Boolean> result = new ArrayList<>();
        for (int[] query : queries) {
            result.add(matrix[query[0]][query[1]]);
        }

        return result;
    }
}