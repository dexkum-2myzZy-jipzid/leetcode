class Solution {
    public int trap(int[] height) {
        // init monotonic stack
        int n = height.length;
        Stack<int[]> stack = new Stack<>();

        int trapArea = 0;
        for (int i = 0; i < n; i++) {
            int h = height[i];
            while (!stack.isEmpty() && stack.peek()[1] < h) {
                int[] last = stack.pop();
                if (stack.isEmpty())
                    break;
                int[] top = stack.peek();
                int dis = (i - top[0] - 1);
                int heightSide = Math.min(top[1], h) - last[1];
                trapArea += (heightSide * dis);
            }

            stack.push(new int[] { i, h });
        }

        return trapArea;
    }
}