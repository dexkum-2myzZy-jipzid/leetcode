class Solution {
    public boolean wordPatternMatch(String pattern, String s) {
        return backtracking(pattern, s, new HashMap<Character, String>(), 0, 0, new HashSet<String>());
    }

    private boolean backtracking(
        String pattern, 
        String s,  
        Map<Character, String> map, 
        int pIndex, 
        int sIndex, 
        Set<String> wordSet){

        if(pIndex == pattern.length()){
            return sIndex == s.length();
        }

        char symbol = pattern.charAt(pIndex);

        // current symbol in maps.keys
        if(map.containsKey(symbol)){
            String word = map.get(symbol);
            if(!s.startsWith(word, sIndex)){
                return false;
            }

            return backtracking(pattern, s, map, pIndex+1, sIndex+word.length(), wordSet);
        }else{
            // current symbol does not in maps.keys
            for(int i = sIndex+1; i <= s.length(); i++){
                String newWord = s.substring(sIndex, i);
                if(wordSet.contains(newWord)){
                    continue;
                }

                map.put(symbol, newWord);
                wordSet.add(newWord);
                // continue to match rest part
                if(backtracking(pattern, s, map, pIndex+1, i, wordSet)){
                    return true;
                }

                map.remove(symbol);
                wordSet.remove(newWord);
            }

            return false;
        }
    }
}