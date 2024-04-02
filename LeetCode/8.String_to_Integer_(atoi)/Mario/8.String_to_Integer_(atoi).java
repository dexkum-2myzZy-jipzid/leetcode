class Solution {
    public int myAtoi(String s) {
        if (s.length() == 0)
            return 0;

        char[] chs = s.toCharArray();

        boolean negative = false;
        long sum = 0;

        // remove white space
        int i = 0;
        while (i < s.length() && chs[i] == ' ') {
            i++;
        }

        if (i >= s.length()) {
            return (int) sum;
        }

        // check '-'
        if (chs[i] == '-') {
            negative = true;
            i += 1;
        } else if (chs[i] == '+') {
            i += 1;
        }

        // sum
        for (; i < s.length(); i++) {
            char c = chs[i];
            int num = c - '0';
            if (num >= 0 && num <= 9) {
                long tmp = sum * 10 + num;
                if (!negative && tmp > Integer.MAX_VALUE) {
                    return Integer.MAX_VALUE;
                } else if (negative && tmp - 1 > Integer.MAX_VALUE) {
                    return Integer.MIN_VALUE;
                } else {
                    sum = tmp;
                }
            } else {
                break;
            }
        }

        // negative
        if (negative) {
            sum = -sum;
        }

        return (int) sum;
    }
}