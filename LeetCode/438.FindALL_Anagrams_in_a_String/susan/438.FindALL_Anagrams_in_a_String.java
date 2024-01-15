class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        int[] target = new int[26];
        int[] current = new int[26];
        int left = 0;
        for(int i = 0; i< p.length(); i++){
            target[p.charAt(i)-'a']++;
        }

        for(int i = 0; i< s.length(); i++){
            current[s.charAt(i)-'a']++;
            if(i - left >= p.length()-1){
                if(Arrays.equals(target,current)){
                    res.add(left);
                }
                current[s.charAt(left)-'a']--;
                left++;
            }
        }

        return res;
    }
}