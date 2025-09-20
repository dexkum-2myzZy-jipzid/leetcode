class Solution {
    public int[] stringIndices(String[] wordsContainer, String[] wordsQuery) {
        int n = wordsContainer.length;
        Trie trie = new Trie();
        for (int i = 0; i < n; i++) {
            trie.insert(wordsContainer[i], i);
        }

        int m = wordsQuery.length;
        int[] res = new int[m];
        for (int i = 0; i < m; i++) {
            String w = wordsQuery[i];
            res[i] = trie.suffixQuery(w);
        }
        return res;
    }
}

class Trie {
    Trie[] children;
    int[] pair; // {index, length}

    Trie() {
        children = new Trie[26];
        pair = new int[] { -1, Integer.MAX_VALUE };
    }

    public void insert(String word, int index) {
        char[] chs = word.toCharArray();
        int n = chs.length;
        Trie node = this;
        if (word.length() < node.pair[1]) {
            node.pair = new int[] { index, word.length() };
        }
        for (int i = n - 1; i >= 0; i--) {
            char c = chs[i];
            if (node.children[c - 'a'] == null) {
                node.children[c - 'a'] = new Trie();
            }
            node = node.children[c - 'a'];
            if (word.length() < node.pair[1]) {
                node.pair = new int[] { index, word.length() };
            }
        }
    }

    public int suffixQuery(String suffix) {
        char[] chs = suffix.toCharArray();
        int n = chs.length;
        Trie node = this;
        for (int i = n - 1; i >= 0; i--) {
            char c = chs[i];
            int idx = c - 'a';
            if (node.children[idx] != null) {
                node = node.children[idx];
            } else {
                break;
            }
        }

        return node.pair[0];
    }
}