class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->dist(b) - dist(a));

        for(int[] point : points){
            pq.add(point);
            if(pq.size()>k){
                pq.poll();
            }
        }

        return pq.toArray(new int[k][2]);
    }

    public int dist(int[] str){
        int x = str[0];
        int y = str[1];
        return x*x+y*y;
    }
}