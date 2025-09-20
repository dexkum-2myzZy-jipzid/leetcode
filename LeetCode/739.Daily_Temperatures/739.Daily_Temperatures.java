class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] result = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            int tmp = temperatures[i];

            while (!stack.isEmpty() && temperatures[stack.peek()] < tmp) {
                int pre = stack.pop();
                result[pre] = i - pre;
            }
            stack.push(i);
        }

        // System.out.println(stack);

        return result;
    }
}