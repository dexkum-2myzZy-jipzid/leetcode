class Solution {
    public List<Integer> diffWaysToCompute(String expression) {
        List<Integer> res = new ArrayList<>();
        int n = expression.length();
        for (int i = 0; i < expression.length(); i++) {
            char c = expression.charAt(i);
            if (c == '+' || c == '-' || c == '*') {
                List<Integer> leftSide = diffWaysToCompute(expression.substring(0, i));
                List<Integer> rightSide = diffWaysToCompute(expression.substring(i + 1, n));
                for (int left : leftSide) {
                    for (int right : rightSide) {
                        int temp = 0;
                        if (c == '+') {
                            temp = left + right;
                        } else if (c == '-') {
                            temp = left - right;
                        } else if (c == '*') {
                            temp = left * right;
                        }
                        res.add(temp);
                    }
                }
            }
        }

        if (res.size() == 0) {
            res.add(Integer.parseInt(expression));
        }

        return res;
    }
}