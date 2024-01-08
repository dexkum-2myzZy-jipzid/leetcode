class MedianFinder {
    private PriorityQueue<Integer> minpq;
    private PriorityQueue<Integer> maxpq;
    public MedianFinder() {
       minpq = new PriorityQueue<>();
       maxpq = new PriorityQueue<Integer>(Collections.reverseOrder());
    }
    
    public void addNum(int num) {
        maxpq.add(num);
        minpq.add(maxpq.poll());
        if(minpq.size()>maxpq.size()){
            maxpq.add(minpq.poll());
        }
    }
    
    public double findMedian() {
        return maxpq.size() == minpq.size()? (maxpq.peek()+ minpq.peek())/2.0: maxpq.peek();
    }
}