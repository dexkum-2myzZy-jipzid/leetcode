class Solution {
    // operation:
    // 1. down: i-1, i can't be 0
    // 2. up: jump = 0, i+2^jump, jump += 1
    private Map<String, Integer> map;

    public int waysToReachStair(int k) {
        map = new HashMap<>();
        return dfs(1, 0, false, k);
    }

    // i: current stair, j: jump times, pre: pre action whether minus one
    // return number of ways Alice can reach stair k.
    private int dfs(int i, int j, boolean pre, int k) {
        if (i > k + 1)
            return 0;

        String key = i + "," + j + "," + pre;
        if (map.containsKey(key))
            return map.get(key);

        int res = 0;
        if (i == k) {
            res = 1;
        }
        res += dfs(i + (1 << j), j + 1, false, k);
        if (!pre && i > 0) {
            res += dfs(i - 1, j, true, k);
        }
        map.put(key, res);
        return res;
    }
}