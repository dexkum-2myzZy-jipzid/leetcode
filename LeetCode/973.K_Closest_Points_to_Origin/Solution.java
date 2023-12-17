class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->dist(b) - dist(a));
        
        for(int[] point: points){
            pq.add(point);
            if(pq.size()>k){
                pq.poll();
            }
        }

        return pq.toArray(new int[k][2]);
    }

    public int dist(int[] a){
        int x = a[0];
        int y = a[1];
        return x*x+y*y;
    }
}