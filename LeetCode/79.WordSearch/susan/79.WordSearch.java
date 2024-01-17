class Solution {
    boolean visited;
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        for(int i = 0; i< m ; i++){
            for(int j = 0; j< n; j++){
                bfs(board,i,j,0,word);
                if(visited){
                    return true;
                }
            }
        }
        return false;
    }

    public void bfs(char[][] board, int i , int j ,int p,String word){
        if(p == word.length()){
            visited = true;
            return;
        }

        if(visited){
            return;
        }

        int m = board.length;
        int n = board[0].length;

        if(i< 0 || i >= m || j <0 || j>= n){
            return;
        }

        if(board[i][j] != word.charAt(p)){
            return;
        }

        board[i][j] = (char)(-board[i][j]);
        bfs(board,i-1,j,p+1,word);
        bfs(board,i,j-1,p+1,word);
        bfs(board,i+1,j,p+1,word);
        bfs(board,i,j+1,p+1,word);
        board[i][j] = (char)(-board[i][j]);

    }
}