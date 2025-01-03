class Solution {
    public int romanToInt(String s) {
        // create map, key is symbols, value is num
        // iterate char in s, previous, current
        // current > previous, e.g.: IV, pre = I, current = V, so sum = (V - I)
        // else: += current

        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        int res = 0;
        int pre = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            int cur = map.get(ch);

            if (cur > pre) {
                res -= 2 * pre;
            }
            res += cur;

            pre = cur;
        }

        return res;
    }
}