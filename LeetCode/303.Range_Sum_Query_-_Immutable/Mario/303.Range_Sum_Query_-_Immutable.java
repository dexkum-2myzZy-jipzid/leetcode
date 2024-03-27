class NumArray {

    private int[] sumArr;

    public NumArray(int[] nums) {
        sumArr = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            sumArr[i] = nums[i];
            if (i - 1 >= 0) {
                sumArr[i] += sumArr[i - 1];
            }
        }
        // System.out.println(Arrays.toString(sumArr));
    }

    public int sumRange(int left, int right) {
        int sum = sumArr[right];
        if (left > 0) {
            sum -= sumArr[left - 1];
        }
        return sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */