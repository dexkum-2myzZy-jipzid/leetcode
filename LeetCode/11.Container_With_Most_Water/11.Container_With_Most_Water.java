class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int max = 0;
        while (left < right) {
            int h = Math.min(height[left], height[right]);
            int area = (right - left) * h;
            max = Math.max(max, area);
            while (left < right && h >= height[right]) {
                right -= 1;
            }
            while (left < right && height[left] <= h) {
                left += 1;
            }
        }
        return max;
    }
}