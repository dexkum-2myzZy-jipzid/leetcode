class Solution {
    int i = 0;
    public int calculate(String s) {
    Stack<Integer> stack = new Stack<Integer>();
    char sign = '+';
    int num = 0;

    while ( i < s.length()) {
        char c = s.charAt(i++);
        if (Character.isDigit(c)) {
            num = 10 * num + (c - '0');
        }
       
        if (c == '(') {
            num = calculate(s);
        }

        if ((!Character.isDigit(c) && c != ' ') || i == s.length()) {
            switch (sign) {
                case '+':
                stack.push(num);
                break;
                case '-':
                stack.push(-num);
                break;
                case '/':
                 stack.push(stack.pop()/num);
                 break;
                case '*':
                 stack.push(stack.pop()*num);
                 break;
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