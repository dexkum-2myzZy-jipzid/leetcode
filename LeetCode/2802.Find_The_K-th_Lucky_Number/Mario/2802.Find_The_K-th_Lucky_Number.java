class Solution {
    public String kthLuckyNumber(int k) {
        k += 1;

        String str = Integer.toBinaryString(k);
        // System.out.println(str);
        int n = str.length();

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < n; i++) {
            if (str.charAt(i) == '0') {
                sb.append(4);
            } else {
                sb.append(7);
            }
        }
        return sb.toString();
    }
}