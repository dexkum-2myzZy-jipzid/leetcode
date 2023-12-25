class Solution {
    public int calculate(String s) {
    Deque<Character> deque = new LinkedList<>();
    for (char c : s.toCharArray()) {
        deque.add(c);
    }
    return helper(deque);
    }

    private int helper(Queue<Character> s) {
    Stack<Integer> stack = new Stack<Integer>();
    char sign = '+';
    int num = 0;

    while (!s.isEmpty()) {
        char c = s.poll();
        if (Character.isDigit(c)) {
            num = 10 * num + (c - '0');
        }
       
        if (c == '(') {
            num = helper(s);
        }

        if ((!Character.isDigit(c) && c != ' ') || s.isEmpty()) {
            if (sign == '+') {
                stack.push(num);
            } else if (sign == '-') {
                stack.push(-num);
            } 
            num = 0;
            sign = c;
        }

                if (c == ')') {
            break;
        }
    }
    int res = 0;
    while(!stack.isEmpty()){
        res += stack.pop();
    }
    return res;
}
}