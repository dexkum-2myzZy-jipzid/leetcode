class Solution {
    public long countAlternatingSubarrays(int[] nums) {

        if (nums.length == 1)
            return 1;

        // nums.length >= 2
        int n = nums.length;
        List<Integer> subArray = new ArrayList<>();

        int pre = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] == nums[i - 1]) {
                subArray.add(i - pre);
                pre = i;
            }
        }
        subArray.add(n - pre);

        long res = 0;
        for (int i = 0; i < subArray.size(); i++) {
            int s = subArray.get(i);
            if (s == 1) {
                res += 1;
            } else {
                res += ((long) (s + 1) * s) / 2;
            }
        }
        return res;
    }
}