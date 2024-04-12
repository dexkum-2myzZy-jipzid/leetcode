class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        // handle edge case
        List<Integer> result = new ArrayList<>();
        if (s.length() < p.length()) {
            return result;
        }

        // count character in p
        int[] pCounter = new int[128];
        for (char ch : p.toCharArray()) {
            pCounter[ch] += 1;
        }

        // for loop characters in s
        int[] sCounter = new int[128];
        char[] chs = s.toCharArray();

        int i = 0;
        for (int j = 0; j < s.length(); j++) {
            if (j < p.length()) {
                sCounter[chs[j]] += 1;
            } else {
                sCounter[chs[i]] -= 1;
                i += 1;
                sCounter[chs[j]] += 1;
            }

            if (j - i + 1 == p.length()) {
                if (Arrays.equals(pCounter, sCounter)) {
                    result.add(i);
                }
            }
        }

        return result;
    }
}