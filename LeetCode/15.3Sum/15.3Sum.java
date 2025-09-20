class Solution {
    private List<List<Integer>> res;

    public List<List<Integer>> threeSum(int[] nums) {
        res = new ArrayList<>();

        Arrays.sort(nums);

        int n = nums.length;
        for (int i = 0; i < n - 2; i++) {
            if (nums[i] > 0) {
                break;
            }

            if (i == 0 || (i > 0 && nums[i] != nums[i - 1])) {
                twoSum(nums, -nums[i], i + 1, n - 1);
            }
        }

        return res;
    }

    private void twoSum(int[] nums, int target, int left, int right) {
        int preLeft = Integer.MAX_VALUE;
        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum > target) {
                right -= 1;
            } else if (sum < target) {
                left += 1;
            } else {
                if (preLeft != nums[left]) {
                    res.add(Arrays.asList(-target, nums[left], nums[right]));
                    preLeft = nums[left];
                }
                left += 1;
                right -= 1;
            }
        }
    }
}

// two sum using Binary Search
class Solution {
    private List<List<Integer>> res;

    public List<List<Integer>> threeSum(int[] nums) {
        res = new ArrayList<>();

        Arrays.sort(nums);

        int n = nums.length;
        for (int i = 0; i < n - 2; i++) {
            if (nums[i] > 0) {
                break;
            }

            if (i == 0 || (i > 0 && nums[i] != nums[i - 1])) {
                twoSum(nums, -nums[i], i + 1, n - 1);
            }
        }

        return res;
    }

    private void twoSum(int[] nums, int target, int left, int right) {
        int mid = 0;
        int preLeft = Integer.MAX_VALUE;
        while (left < right) {
            mid = (left + right) / 2;
            int sum = nums[left] + nums[right];
            if (sum == target) {
                if (preLeft != nums[left]) {
                    res.add(Arrays.asList(-target, nums[left], nums[right]));
                    preLeft = nums[left];
                }
                left += 1;
                right -= 1;
            } else if (sum > target) {
                if (nums[mid] + nums[left] > target) {
                    right = mid - 1;
                } else {
                    right -= 1;
                }
            } else {
                if (nums[mid] + nums[right] < target) {
                    left = mid + 1;
                } else {
                    left += 1;
                }
            }
        }
    }
}