class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        int res = -1;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                return mid;
            }

            if (nums[mid] >= nums[left]) {
                if (target < nums[mid] && target >= nums[left]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return res;
    }
}

// find pivot(most samllest point), then binary search two side
class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        int left = 0, right = n - 1;

        // find smallest element - pivot
        while (left <= right) {
            int m = (left + right) / 2;
            if (nums[m] > nums[n - 1]) {
                left = m + 1;
            } else {
                right = m - 1;
            }
        }

        // binary search left side, then right side
        int res = binarySearch(nums, 0, left - 1, target);
        if (res != -1)
            return res;

        return binarySearch(nums, left, n - 1, target);
    }

    private int binarySearch(int[] nums, int left, int right, int target) {
        while (left <= right) {
            int m = (left + right) / 2;
            if (nums[m] == target) {
                return m;
            } else if (nums[m] > target) {
                right = m - 1;
            } else {
                left = m + 1;
            }
        }
        return -1;
    }
}