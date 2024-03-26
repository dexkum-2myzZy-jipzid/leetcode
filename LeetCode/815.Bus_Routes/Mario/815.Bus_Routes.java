class Solution {
    public int numBusesToDestination(int[][] routes, int source, int target) {
        // handle corner case
        if (source == target)
            return 0;

        // create graph, stop -> route index
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < routes.length; i++) {
            for (int stop : routes[i]) {
                List<Integer> list = graph.getOrDefault(stop, new ArrayList<>());
                list.add(i);
                graph.put(stop, list);
            }
        }

        // bfs
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        if (graph.get(source) == null)
            return -1;
        for (int index : graph.get(source)) {
            queue.offer(index);
            visited.add(index);
        }
        int bus = 1;

        while (!queue.isEmpty()) {
            int n = queue.size();
            for (int i = 0; i < n; i++) {
                int index = queue.poll();

                int[] route = routes[index];
                for (int stop : route) {

                    if (stop == target) {
                        return bus;
                    }

                    for (int idx : graph.get(stop)) {
                        if (!visited.contains(idx)) {
                            visited.add(idx);
                            queue.offer(idx);
                        }
                    }

                }
            }
            bus += 1;
        }

        return -1;
    }
}