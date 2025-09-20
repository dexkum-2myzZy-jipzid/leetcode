class Solution {
    public boolean isValid(String s) {
        int top = -1;
        char[] arr = new char[s.length()];

        for (char ch : s.toCharArray()) {
            if (ch == '{' || ch == '(' || ch == '[') {
                top += 1;
                arr[top] = ch;
            } else if ((ch == ']' && top >= 0 && arr[top] == '[')
                    || (ch == ')' && top >= 0 && arr[top] == '(')
                    || (ch == '}' && top >= 0 && arr[top] == '{')) {
                top -= 1;
            } else {
                return false;
            }
        }

        return top == -1;
    }
}