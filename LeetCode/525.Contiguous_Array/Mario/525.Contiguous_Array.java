class Solution {
    public int findMaxLength(int[] nums) {
        int zero = 0, one = 0;
        int res = 0;

        Map<Integer, Integer> countIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (num == 0) {
                zero += 1;
            } else {
                one += 1;
            }

            if (countIndex.get(one - zero) == null) {
                countIndex.put(one - zero, i);
            }

            if (zero == one) {
                res = Math.max(res, zero + one);
            } else if (countIndex.get(one - zero) != null) {
                int index = countIndex.get(one - zero);
                res = Math.max(res, i - index);
            }
        }

        return res;
    }
}