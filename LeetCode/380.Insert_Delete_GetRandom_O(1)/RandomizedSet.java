class RandomizedSet {

    List<Integer> nums;
    HashMap<Integer,Integer> numToIndex;

    public RandomizedSet() {
        nums = new ArrayList<Integer>();
        numToIndex = new HashMap<>();
    }
    
    public boolean insert(int val) {
        if(numToIndex.containsKey(val)){
            return false;
        }
        numToIndex.put(val,nums.size());
            nums.add(val);
            return true;
    }
    
    public boolean remove(int val) {
        if(!numToIndex.containsKey(val)){
             return false;
        }
        int index = numToIndex.get(val);
        numToIndex.put(nums.get(nums.size()-1),index);
        Collections.swap(nums,index,nums.size()-1);
        nums.remove(nums.size()-1);
        numToIndex.remove(val);
        return true;
    }
    
    public int getRandom() {
        return nums.get((int)(Math.random()*nums.size()));
    }
}