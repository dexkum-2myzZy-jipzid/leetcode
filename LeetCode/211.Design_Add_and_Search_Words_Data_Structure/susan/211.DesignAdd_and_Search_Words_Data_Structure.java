class WordDictionary {

    TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode node = root;
        for(char c : word.toCharArray()){
            if(node.children[c-'a']== null){
                node.children[c-'a'] = new TrieNode();
            }
            node = node.children[c-'a'];
        }
        node.isWork = true;
    }
    
    public boolean search(String word) {
        return helper(word,0,root);
    }

    public boolean helper(String word, int position, TrieNode node){
         if(position == word.length()){
             return node.isWork;
         }
         char c = word.charAt(position);
         if( c != '.'){
             return node.children[c-'a'] != null && helper(word, position+1,node.children[c-'a']);
         }

         for(int i = 0; i< 26; i++){
             if(node.children[i] != null && helper(word,position+1,node.children[i])){
                 return true;
             }
         }

         return false;
    }
}
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isWork;
}