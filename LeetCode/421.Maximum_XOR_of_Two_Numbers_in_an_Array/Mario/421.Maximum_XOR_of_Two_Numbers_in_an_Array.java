class Solution {
    public int findMaximumXOR(int[] nums) {
        int maxNum = 0;
        for (int num : nums) {
            maxNum = Math.max(maxNum, num);
        }

        int highBit = 0;
        while ((maxNum >> 1) != 0) {
            maxNum >>= 1;
            highBit += 1;
        }

        int result = 0, mask = 0;
        Set<Integer> seen = new HashSet<>();
        for (int i = highBit; i >= 0; i--) {
            seen.clear();
            mask |= (1 << i);
            int newResult = result | (1 << i);

            for (int num : nums) {
                num &= mask;
                if (seen.contains(newResult ^ num)) {
                    result = newResult;
                    break;
                }
                seen.add(num);
            }
        }

        return result;
    }
}