class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for (String str : tokens) {
            switch (str) {
                case "+":
                    int a = stack.pop(), b = stack.pop();
                    stack.push(a + b);
                    break;
                case "-":
                    int c = stack.pop(), d = stack.pop();
                    stack.push(d - c);
                    break;
                case "/":
                    int e = stack.pop(), f = stack.pop();
                    stack.push(f / e);
                    break;
                case "*":
                    int g = stack.pop(), h = stack.pop();
                    stack.push(g * h);
                    break;
                default:
                    stack.push(Integer.parseInt(str));
            }
        }

        return stack.pop();
    }
}