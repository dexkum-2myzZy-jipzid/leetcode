class Solution {
    public int findMaximumXOR(int[] nums) {
      int res = Integer.MIN_VALUE;
      TrieNode root = new TrieNode();
      for(int num : nums){
          root.addNum(root,num);
      }
      for(int num : nums){
          res = Math.max(root.findMaxXor(root,num),res);
      }
      return res;
    }
}
class TrieNode{
    TrieNode[] children;

    public TrieNode(){
        children = new TrieNode[2];
    }

    public void addNum(TrieNode root, int num){
        TrieNode node = root;
        for(int i = 31; i>= 0; i--){
            int curBit = (num>>i) & 1;
            if(node.children[curBit] == null){
                node.children[curBit] = new TrieNode();
            }
               node = node.children[curBit];
        }
    }

    public int findMaxXor(TrieNode root, int num){
        int sum = 0;
        TrieNode node = root;
        for(int i = 31; i>= 0; i--){
            int curBit = (num >> i ) & 1;
            int otherBit = curBit == 1? 0:1;
            if(node.children[otherBit] == null){
                node = node.children[curBit];
            }else{
                sum += (1 << i) ;
                node = node.children[otherBit];
            }
        }
        return sum;
    }

}