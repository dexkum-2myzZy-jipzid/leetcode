class Solution {
    Set<String> res = new HashSet<>();
    public List<String> findWords(char[][] board, String[] words) {
       int m = board.length; 
       int n = board[0].length;
       Trie trie = new Trie(); 
       for(String word: words){
           trie.insert(word);
       }
       boolean[][] visited = new boolean[m][n];
       for(int i = 0; i< m; i++){
           for(int j = 0; j< n; j++){
               bfs(board,visited,"",i,j,trie);
           }
       }
       return new ArrayList<>(res);
    }

    public void bfs(char[][] board, boolean[][] visited,String str,int i, int j, Trie trie){
        if(i< 0 || j< 0|| i>= board.length || j >= board[0].length){
            return;
        }

        if(visited[i][j]){
            return;
        }

        str +=board[i][j];

        if(!trie.startWith(str)){
             return;
        }

        if(trie.search(str)){
            res.add(str);
        }

        visited[i][j] = true;
        bfs(board,visited,str,i-1,j,trie);
        bfs(board,visited,str,i,j-1,trie);
        bfs(board,visited,str,i+1,j,trie);
        bfs(board,visited,str,i,j+1,trie);
        visited[i][j] = false;
    }
}
class Trie{
    TrieNode root;

    public Trie(){
        root = new TrieNode();
    }

    public void insert(String word){
        TrieNode node = root;
        for(char c : word.toCharArray()){
            if(node.children[c-'a'] == null){
                node.children[c-'a'] = new TrieNode();
            }
            node = node.children[c-'a'];
        }
        node.isWork = true;
    }

    public boolean search(String word){
        TrieNode node = root;
        for(char c : word.toCharArray()){
            if(node.children[c-'a'] == null){
                return false;
            }
            node = node.children[c-'a'];
        }

        return node.isWork;
    }

    public boolean startWith(String prefix){
        TrieNode node = root;
        for(char c : prefix.toCharArray()){
            if(node.children[c-'a']== null){
                return false;
            }
            node = node.children[c-'a'];
        }
        return true;
    }
}

class TrieNode{
    TrieNode[] children = new TrieNode[26];
    boolean isWork;
}