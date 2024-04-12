class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        // handle corner case
        if (s.length() <= 10 || s.length() > 100000) {
            return new ArrayList<>();
        }
        Set<String> seen = new HashSet(), result = new HashSet();
        for (int i = 10; i <= s.length(); i++) {
            String subStr = s.substring(i - 10, i);
            if (!seen.add(subStr)) {
                result.add(subStr);
            }
        }
        return new ArrayList<>(result);
    }
}

// Rabin-Karp
