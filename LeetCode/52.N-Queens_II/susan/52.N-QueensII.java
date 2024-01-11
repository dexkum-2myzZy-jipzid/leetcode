class Solution {
    int res = 0;

    public int totalNQueens(int n) {
        List<String> track = new ArrayList<>();

        for(int i = 0; i< n ; i++){
            StringBuilder sb = new StringBuilder();
            for(int j = 0; j < n ;j++){
                sb.append(".");
            }
            track.add(sb.toString());
        }

        backtrack(track,0);
        return res;
    }

    void backtrack(List<String> board, int row) {
       
        if (row == board.size()) {
            res++;
            return;
        }
        
        int n = board.get(row).length();
        for (int col = 0; col < n; col++) {
            
            if (!isValid(board, row, col)) {
                continue;
            }
            
            StringBuilder sb = new StringBuilder(board.get(row));
            sb.setCharAt(col, 'Q');
            board.set(row, sb.toString());

           
            backtrack(board, row + 1);
           
            sb.setCharAt(col, '.');
            board.set(row, sb.toString());
        }
    }

   boolean isValid(List<String> board, int row, int col) {
    int n = board.size();
    
    for (int i = 0; i <= row; i++) {
        if (board.get(i).charAt(col) == 'Q')
            return false;
    }
    
    for (int i = row - 1, j = col + 1; 
            i >= 0 && j < n; i--, j++) {
        if (board.get(i).charAt(j) == 'Q')
            return false;
    }
   
    for (int i = row - 1, j = col - 1;
            i >= 0 && j >= 0; i--, j--) {
        if (board.get(i).charAt(j) == 'Q')
            return false;
    }
    return true;
}
}