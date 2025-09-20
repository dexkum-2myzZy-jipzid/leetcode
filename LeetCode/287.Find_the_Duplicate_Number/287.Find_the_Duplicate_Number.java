class Solution {
    public int findDuplicate(int[] nums) {
        int[] arr = new int[nums.length];
        for (int n : nums) {
            arr[n - 1] += 1;
            if (arr[n - 1] > 1)
                return n;
        }
        return -1;
    }
}