class Solution {
    public int maxFrequencyElements(int[] nums) {
        int max = 0;
        int res = 0;
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int num : nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        
        for(int i : map.keySet()){
            max = Math.max(max, map.get(i));
        }
        
        for(int i : map.keySet()){
            if(map.get(i) == max){
                res +=map.get(i);
            }
        }
        
        
        return res;
        
    }
}