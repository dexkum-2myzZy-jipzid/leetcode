class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] res1 = new int[nums1.length];
        HashMap<Integer,Integer> map = new HashMap<>();
        Stack<Integer> s = new Stack<>();

        for(int i = nums2.length - 1; i>= 0; i--){
           while(!s.isEmpty() && s.peek() <= nums2[i]){
               s.pop();
           }
           int res = s.isEmpty()? -1:s.peek();
           map.put(nums2[i],res);
           s.push(nums2[i]);
        }

        for(int j = 0; j< nums1.length ; j++){
            if(map.containsKey(nums1[j])){
                res1[j] = map.get(nums1[j]);
            }
        }

        return res1;

    }
}