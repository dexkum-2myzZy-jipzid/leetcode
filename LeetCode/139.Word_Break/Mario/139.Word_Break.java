class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int i = 1; i <= s.length(); i++) {
            for (String word : wordDict) {
                int n = word.length();
                if (i >= n && dp[i - n] && word.equals(s.substring(i - n, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[dp.length - 1];
    }
}

// Trie
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        // Trie store words
        Trie t = new Trie();
        for (String w : wordDict) {
            char[] chs = w.toCharArray();
            Trie node = t;
            for (int i = 0; i < chs.length; i++) {
                int index = chs[i] - 'a';
                if (node.children[index] == null) {
                    node.children[index] = new Trie();
                }
                node = node.children[index];
            }
            node.isEnd = true;
        }

        // search
        boolean[] dp = new boolean[s.length()];
        for (int i = 0; i < s.length(); i++) {
            // dp[i-1] is true, it's necessary to continue
            if (i == 0 || dp[i - 1]) {
                Trie node = t;
                for (int j = i; j < s.length(); j++) {
                    int index = s.charAt(j) - 'a';
                    // no word
                    if (node.children[index] == null) {
                        break;
                    }

                    node = node.children[index];
                    // reach word end
                    if (node.isEnd) {
                        dp[j] = true;
                    }
                }
            }
        }

        return dp[s.length() - 1];
    }
}

class Trie {
    public Trie[] children;
    public boolean isEnd;

    public Trie() {
        children = new Trie[26];
        isEnd = false;
    }
}