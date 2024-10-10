// 1. sliding window & binary search
class Solution {
    public int characterReplacement(String s, int k) {
        int left = 1, right = s.length() + 1;
        while (left + 1 < right) {
            int mid = (left + right) / 2;
            if (helper(s, mid, k)) {
                left = mid;
            } else {
                right = mid;
            }
        }

        return left;
    }

    private boolean helper(String s, int len, int k) {
        int[] freqMap = new int[26];
        int maxFreq = 0, start = 0;
        for (int end = 0; end < s.length(); end += 1) {
            freqMap[s.charAt(end) - 'A'] += 1;

            if (end + 1 - start > len) {
                freqMap[s.charAt(start) - 'A'] -= 1;
                start += 1;
            }

            maxFreq = Math.max(maxFreq, freqMap[s.charAt(end) - 'A']);
            if (len <= maxFreq + k) {
                return true;
            }
        }
        return false;
    }
}

// 2. sliding window
class Solution {
    public int characterReplacement(String s, int k) {

        int[] freqMap = new int[26];
        int maxFreq = 0;
        int start = 0;
        int result = 0;

        for (int end = 0; end < s.length(); end += 1) {
            int curChar = s.charAt(end) - 'A';
            freqMap[curChar] += 1;

            maxFreq = Math.max(maxFreq, freqMap[curChar]);

            if (end + 1 - start > maxFreq + k) {
                int outgoingChar = s.charAt(start) - 'A';
                freqMap[outgoingChar] -= 1;
                start += 1;
            }

            result = end + 1 - start;
        }

        return result;
    }
}