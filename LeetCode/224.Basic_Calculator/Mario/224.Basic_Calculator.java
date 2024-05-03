class Solution {
    public int calculate(String s) {
        s = s.replaceAll(" ", "");
        int res = 0, num = 0, sign = 1;
        Stack<Integer> stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                stack.push(res);
                stack.push(sign);
                res = 0;
                sign = 1;
            } else if (ch == ')') {
                res += sign * num;
                res *= stack.pop();
                res += stack.pop();
                num = 0;
            } else if (ch == '-') {
                res += (num * sign);
                sign = -1;
                num = 0;
            } else if (ch == '+') {
                res += (num * sign);
                sign = 1;
                num = 0;
            } else {
                num = 10 * num + (ch - '0');
            }
        }

        return res + sign * num;
    }

}