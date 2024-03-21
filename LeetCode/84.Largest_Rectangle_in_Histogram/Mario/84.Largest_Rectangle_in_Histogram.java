class Solution {
    public int largestRectangleArea(int[] heights) {
        // init monotonic stack
        Stack<int[]> stack = new Stack<>();
        int maxArea = 0;
        int n = heights.length;

        // manipulate monotonic stack
        for (int i = 0; i < n; i++) {
            int h = heights[i], start = i;

            while (!stack.isEmpty() && stack.peek()[1] > h) {
                int[] last = stack.pop();
                maxArea = Math.max(maxArea, last[1] * (i - last[0]));
                start = last[0];
            }

            stack.push(new int[] { start, h });
        }

        // caculate left elements in stack
        for (int[] e : stack) {
            maxArea = Math.max(maxArea, (n - e[0]) * e[1]);
        }

        return maxArea;
    }
}