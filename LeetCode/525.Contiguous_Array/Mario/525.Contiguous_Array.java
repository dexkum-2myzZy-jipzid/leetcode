class Solution {
    public int findMaxLength(int[] nums) {
        int n = nums.length;

        Map<Integer, Integer> map = new HashMap<>();
        int ones = 0, zeros = 0;
        map.put(ones - zeros, -1);

        int res = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                ones += 1;
            } else {
                zeros += 1;
            }

            Integer idx = map.get(ones - zeros);
            if (idx == null) {
                map.put(ones - zeros, i);
            } else {
                res = Math.max(res, i - idx);
            }
        }

        return res;
    }
}