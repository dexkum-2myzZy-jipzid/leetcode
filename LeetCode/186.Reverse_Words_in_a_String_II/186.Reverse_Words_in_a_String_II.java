class Solution {
    public void reverseWords(char[] s) {
        // is blue -> eulb si -> blue is
        int left = 0, right = s.length - 1;
        reverseRange(s, left, right);

        Queue<Integer> spacePos = new LinkedList<>();
        for (int i = 0; i < s.length; i++) {
            if (s[i] == ' ') {
                spacePos.offer(i);
            }
        }
        spacePos.offer(s.length);

        left = 0;
        while (!spacePos.isEmpty()) {
            int pos = spacePos.poll();
            right = pos - 1;
            reverseRange(s, left, right);
            left = pos + 1;
        }
    }

    private void reverseRange(char[] s, int left, int right) {
        while (left < right) {
            swap(s, left, right);
            left += 1;
            right -= 1;
        }
    }

    private void swap(char[] s, int i, int j) {
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }
}