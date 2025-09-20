class Solution {
    public int threeSumClosest(int[] nums, int target) {
        // sort nums, then interate the every elements in the nums
        // [-1, 1, 2, 4], i = 0, the rest array, two pointer
        Arrays.sort(nums);
        int n = nums.length;
        int res =  100000;
        for(int i = 0; i < n; i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }

            int l = i+1, r = n-1;
            while(l < r){
                int sum = nums[i] + nums[l] + nums[r];
                if(sum == target){
                    return sum;
                }else if(sum > target){
                    r -= 1;
                }else{
                    l += 1;
                }

                if(Math.abs(sum - target) < Math.abs(res - target)){
                    res = sum;
                }
            }
        }

        return res;
    }
}