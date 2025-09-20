class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int left = 0, right = n - 1;
        int i = n - 1;
        while (left <= right && i >= 0) {
            int l = Math.abs(nums[left]), r = Math.abs(nums[right]);
            if (r > l) {
                res[i] = r * r;
                right -= 1;
            } else {
                res[i] = l * l;
                left += 1;
            }
            i -= 1;
        }

        return res;
    }
}