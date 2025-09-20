class Solution {
    public int findMaximumXOR(int[] nums) {
        int maxNum = 0;
        for (int num : nums) {
            maxNum = Math.max(maxNum, num);
        }

        int highBit = 0;
        while ((maxNum >> 1) != 0) {
            maxNum >>= 1;
            highBit += 1;
        }

        int result = 0, mask = 0;
        Set<Integer> seen = new HashSet<>();
        for (int i = highBit; i >= 0; i--) {
            seen.clear();
            mask |= (1 << i);
            int newResult = result | (1 << i);

            for (int num : nums) {
                num &= mask;
                if (seen.contains(newResult ^ num)) {
                    result = newResult;
                    break;
                }
                seen.add(num);
            }
        }

        return result;
    }
}

// using Trie to solve this leetcode
class Solution {
    public int findMaximumXOR(int[] nums) {
        // get maximum binary length
        int maxNum = 0;
        for (int num : nums) {
            maxNum = Math.max(maxNum, num);
        }
        int len = Integer.toBinaryString(maxNum).length();
        int maxXor = 0;

        // iterate element in nums
        TrieNode root = new TrieNode();
        for (int num : nums) {
            TrieNode node = root, xorNode = root;
            int curXor = 0;

            for (int i = len - 1; i >= 0; i--) {
                int bit = (num >> i) & 1;
                int toggledBit = bit ^ 1;

                if (node.children[bit] == null) {
                    node.children[bit] = new TrieNode();
                }
                node = node.children[bit];

                if (xorNode.children[toggledBit] != null) {
                    curXor |= (1 << i);
                    xorNode = xorNode.children[toggledBit];
                } else {
                    xorNode = xorNode.children[bit];
                }
            }

            maxXor = Math.max(maxXor, curXor);
        }

        return maxXor;
    }
}

class TrieNode {
    TrieNode children[];

    TrieNode() {
        this.children = new TrieNode[2];
    }
}