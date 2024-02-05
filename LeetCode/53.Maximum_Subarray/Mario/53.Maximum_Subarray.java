class Solution {
    public int maxSubArray(int[] nums) {
        int current_max = 0, global_max = Integer.MIN_VALUE;

        for (int i = 0; i < nums.length; i++) {
            current_max += nums[i];
            if (current_max > global_max) {
                global_max = current_max;
            }

            if (current_max < 0) {
                current_max = 0;
            }
        }

        return global_max;
    }
}

// second time to solve this problem
class Solution {
    public int maxSubArray(int[] nums) {
        int globalSum = nums[0], currSum = nums[0];

        for (int j = 1; j < nums.length; j++) {
            if (currSum <= 0) {
                currSum = nums[j];
            } else {
                currSum += nums[j];
            }
            if (globalSum < currSum) {
                globalSum = currSum;
            }
        }

        return globalSum;
    }
}

// third time to solve this problem using Divide & conquer
class Solution {
    public int maxSubArray(int[] nums) {
        return maxSubArray(nums, 0, nums.length - 1);
    }

    private int maxSubArray(int[] nums, int left, int right) {
        if (left == right) {
            return nums[left];
        }

        int mid = (right + left) / 2;
        int leftSum = maxSubArray(nums, left, mid);
        int rightSum = maxSubArray(nums, mid + 1, right);
        int crossSum = crossSum(nums, left, mid, right);

        return Math.max(Math.max(leftSum, rightSum), crossSum);
    }

    private int crossSum(int[] nums, int left, int mid, int right) {
        int leftSum = Integer.MIN_VALUE, rightSum = Integer.MIN_VALUE;
        int sum = 0;

        for (int i = mid; i >= left; i--) {
            sum += nums[i];
            leftSum = Math.max(leftSum, sum);
        }

        sum = 0;
        for (int i = mid + 1; i <= right; i++) {
            sum += nums[i];
            rightSum = Math.max(rightSum, sum);
        }

        return leftSum + rightSum;
    }
}