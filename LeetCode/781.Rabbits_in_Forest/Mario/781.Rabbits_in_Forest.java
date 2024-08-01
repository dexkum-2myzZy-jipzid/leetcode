class Solution {
    public int numRabbits(int[] answers) {
        // {2:2, 3:1} [1, 1, 2]
        // {2:3, 3:1} [1, 1, 1, 2]
        Map<Integer, Integer> counter = new HashMap<>();
        for (int ans : answers) {
            counter.put(ans + 1, counter.getOrDefault(ans + 1, 0) + 1);
        }

        int result = 0;
        for (int key : counter.keySet()) {
            int cnt = counter.get(key);
            int group = cnt / key;
            int remainder = cnt - key * group;
            group += (remainder > 0 ? 1 : 0);
            result += group * key;
        }

        return result;
    }
}
