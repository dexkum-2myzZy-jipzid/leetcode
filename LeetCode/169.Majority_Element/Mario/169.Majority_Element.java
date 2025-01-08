class Solution {
    public int majorityElement(int[] nums) {
        Integer candidate = null;
        int count = 0;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }

            if (candidate == num) {
                count += 1;
            } else {
                count -= 1;
            }
        }

        return candidate;
    }
}