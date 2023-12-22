class Solution {
    public int minKnightMoves(int x, int y) {
       int[][] offsets = {{-2,-1},{-1,-2},{-2,1},{-1,2},{1,-2},{2,-1},{2,1},{1,2}}; 

       boolean[][] visited = new boolean[607][607];

       Queue<int[]> q = new LinkedList<>();
       q.offer(new int[]{0,0});
       int steps = 0;

       while(!q.isEmpty()){
           int curLevel = q.size();
           for(int i = 0; i< curLevel; i++){
               int[] cur = q.poll();
               if(cur[0] == x && cur[1] == y){
                   return steps;
               }

               for(int[] offset: offsets){
                   int[] next = new int[]{cur[0]+offset[0],cur[1]+offset[1]};

                   if(!visited[next[0]+302][next[1]+302]){
                       visited[next[0]+302][next[1]+302] = true;
                        q.offer(next);
                   }
               }
           }
           steps++;
       }

       return steps;
    }
}