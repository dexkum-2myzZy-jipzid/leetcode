class Solution {
    public int firstUniqChar(String s) {
       int index = Integer.MAX_VALUE;
       HashMap<Character,Integer> count = new HashMap<>();
       for(char c: s.toCharArray()){
           count.put(c,count.getOrDefault(c,0)+1);
       }

       for(int i = 0; i< s.length(); i++){
           if(count.get(s.charAt(i)) ==1){
               index = Math.min(index,i);
           }
       }

       return index == Integer.MAX_VALUE ? -1:index;
    }
}