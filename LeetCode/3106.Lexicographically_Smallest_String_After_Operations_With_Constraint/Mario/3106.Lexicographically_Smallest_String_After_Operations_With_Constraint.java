class Solution {
    public String getSmallestString(String s, int k) {
        char[] chs = s.toCharArray();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < chs.length; i++) {
            char c = chs[i];
            if (k <= 0) {
                sb.append(c);
            } else {
                int distance = Math.min(c - 'a', 26 - c + 'a');
                if (distance <= k) {
                    k -= distance;
                    sb.append('a');
                } else if (distance > k) {
                    char b = (char) (c - k);
                    k = 0;
                    sb.append(b);
                }
            }
        }

        return sb.toString();

    }
}