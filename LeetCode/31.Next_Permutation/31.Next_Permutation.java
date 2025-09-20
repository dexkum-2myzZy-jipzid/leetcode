class Solution {
    public void nextPermutation(int[] nums) {
        // find first decrese num, then find first large num in the right side,
        // then swap and reverse them

        // find first decreasing element from the right -> index: i...n-1 is decreasing
        // array
        int n = nums.length;
        int i = n - 2;
        while (i >= 0 && nums[i + 1] <= nums[i]) {
            i--;
        }

        // If such an element is found, find the smallest larger element to its right
        if (i >= 0) {
            // System.out.println("i:" + i + "\t nums[i]:" + nums[i]);
            int j = n - 1;
            while (nums[j] <= nums[i]) {
                j -= 1;
            }
            swap(nums, i, j);
        }

        // reverse the elements to the right of the pivot (i+1)
        // System.out.println(Arrays.toString(nums));
        reverse(nums, i + 1);
        // System.out.println(Arrays.toString(nums));
    }

    private void reverse(int[] nums, int start) {
        int i = start, j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}