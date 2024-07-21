class Solution {
    public int subarraySum(int[] nums, int k) {
        // prefixsum + map
        // map key: prefixSum, value: count
        // (currentSum - k) == key,if exist, result += count
        int currentSum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int result = 0;
        for (int i = 0; i < nums.length; i++) {
            currentSum += nums[i];
            int diff = currentSum - k;
            if (map.containsKey(diff)) {
                result += map.get(diff);
            }
            int count = map.getOrDefault(currentSum, 0) + 1;
            map.put(currentSum, count);
        }

        return result;
    }
}