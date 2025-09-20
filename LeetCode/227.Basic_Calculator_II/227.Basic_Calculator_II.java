class Solution {
    public int calculate(String s) {
        if (s == null && s.isEmpty())
            return 0;

        int n = s.length();
        Stack<Integer> stack = new Stack<>();
        int curNum = 0;
        int operation = '+';

        for (int i = 0; i < n; i++) {
            char cur = s.charAt(i);
            if (isDigit(cur)) {
                curNum = curNum * 10 + cur - '0';
            }

            // Perform the operation if the current character is not a digit, not a
            // whitespace, or if it is the last element
            if (!isDigit(cur) && cur != ' ' || i == n - 1) {
                if (operation == '+') {
                    stack.push(curNum);
                } else if (operation == '-') {
                    stack.push(-curNum);
                } else if (operation == '*') {
                    stack.push(stack.pop() * curNum);
                } else if (operation == '/') {
                    stack.push(stack.pop() / curNum);
                }
                curNum = 0;
                operation = cur;
            }
        }

        int result = 0;
        while (!stack.isEmpty()) {
            result += stack.pop();
        }
        return result;
    }

    private boolean isDigit(char ch) {
        return ch >= '0' && ch <= '9';
    }
}