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
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        // base value
        int l = 10;
        if (s.length() <= l)
            return new ArrayList();
        int a = 4, al = (int) Math.pow(4, l);

        Map<Character, Integer> toInt = new HashMap() {
            {
                put('A', 0);
                put('C', 1);
                put('G', 2);
                put('T', 3);
            }
        };

        int[] nums = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            nums[i] = toInt.get(s.charAt(i));
        }

        int h = 0;
        Set<Integer> seen = new HashSet<>();
        Set<String> result = new HashSet<>();
        for (int i = l - 1; i < s.length(); i++) {
            if (i == l - 1) {
                for (int j = 0; j < l; j++) {
                    h = h * a + nums[j];
                }
            } else {
                h = h * a - nums[i - l] * al + nums[i];
            }

            if (seen.contains(h)) {
                result.add(s.substring(i - l + 1, i + 1));
            }
            seen.add(h);
        }

        return new ArrayList<>(result);
    }
}