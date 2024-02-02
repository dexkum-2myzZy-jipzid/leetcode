class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        Map<String, Integer> counter = new HashMap<>();
        for (String word : words) {
            counter.put(word, counter.getOrDefault(word, 0) + 1);
        }

        List<Integer> res = new ArrayList<>();

        int wordLen = words[0].length();
        for (int i = 0; i < wordLen; i++) {
            int left = i, right = i, count = 0;

            Map<String, Integer> cur = new HashMap<>();

            while (right + wordLen <= s.length()) {
                String rWord = s.substring(right, right + wordLen);
                right += wordLen;

                if (counter.containsKey(rWord)) {
                    cur.put(rWord, cur.getOrDefault(rWord, 0) + 1);
                    count += 1;
                    while (cur.get(rWord) > counter.get(rWord)) {
                        String lword = s.substring(left, left + wordLen);
                        left += wordLen;
                        cur.put(lword, cur.get(lword) - 1);
                        count -= 1;
                    }

                    if (count == words.length) {
                        res.add(left);
                    }
                } else {
                    cur.clear();
                    left = right;
                    count = 0;
                }
            }
        }
        return res;
    }
}