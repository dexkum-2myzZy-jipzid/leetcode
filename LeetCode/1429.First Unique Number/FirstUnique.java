class FirstUnique {

    HashMap<Integer,Integer> count = new HashMap<>();
    Queue<Integer> q= new LinkedList<>();

    public FirstUnique(int[] nums) {
        for(int num:nums){
            q.offer(num);
            count.put(num,count.getOrDefault(num,0)+1);
        }
    }
    
    public int showFirstUnique() {
        while(!q.isEmpty()){
            int digit = q.peek();
            if(count.get(digit) > 1){
                q.poll();
            }else{
                return digit;
            }
        }
        return -1;
    }
    
    public void add(int value) {
        q.offer(value);
        count.put(value,count.getOrDefault(value,0)+1);
    }
}