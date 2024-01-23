class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1, j = b.length() - 1;
        int plus = 0, sum = 0;
        while (i >= 0 || j >= 0) {
            sum = plus;
            if (i >= 0) {
                sum += a.charAt(i) - '0';
                i -= 1;
            }

            if (j >= 0) {
                sum += b.charAt(j) - '0';
                j -= 1;
            }
            plus = sum > 1 ? 1 : 0;
            sb.append(sum % 2);
        }

        if (plus > 0)
            sb.append(plus);

        return sb.reverse().toString();
    }
}