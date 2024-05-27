class Solution {
    public String compressedString(String word) {
        StringBuilder sb = new StringBuilder();
        int count = 1;
        char pre = word.charAt(0);
        for (int i = 1; i < word.length(); i++) {
            char current = word.charAt(i);
            if (pre == current) {
                count += 1;
                if (count == 9) {
                    sb.append(count);
                    sb.append(pre);
                    count = 0;
                    pre = current;
                }
            } else {
                if (count == 0) {
                    pre = current;
                    count = 1;
                    continue;
                }
                sb.append(count);
                sb.append(pre);
                count = 1;
                pre = current;
            }
        }

        if (count != 0) {
            sb.append(count);
            sb.append(pre);
        }

        return sb.toString();
    }
}