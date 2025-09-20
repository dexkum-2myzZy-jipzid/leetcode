class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        // convert wall to be prefix sum
        // using set to record prefix sum number
        Map<Integer, Integer> counter = new HashMap<>();
        for (List<Integer> w : wall) {
            List<Integer> list = new ArrayList<>();
            int prefix = 0;
            for (int i = 0; i < w.size() - 1; i++) {
                prefix += w.get(i);
                int count = counter.getOrDefault(prefix, 0) + 1;
                counter.put(prefix, count);
            }
        }

        int maxFreq = 0;
        for (int key : counter.keySet()) {
            maxFreq = Math.max(counter.get(key), maxFreq);
        }

        return wall.size() - maxFreq;
    }
}