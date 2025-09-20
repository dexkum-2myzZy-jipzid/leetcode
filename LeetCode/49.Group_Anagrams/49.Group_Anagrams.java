class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();

        Map<Integer, List<String>> map = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            char[] chs = strs[i].toCharArray();
            int[] counter = new int[26];
            for (char c : chs) {
                counter[c - 'a'] += 1;
            }

            int hash = toHash(counter);

            List<String> values = map.get(hash);
            if (values == null) {
                values = new ArrayList<>();
                values.add(strs[i]);
                map.put(hash, values);
                res.add(values);
            } else {
                values.add(strs[i]);
            }
        }

        return res;
    }

    private int toHash(int[] arr) {
        int hash = 0;
        for (int i = 0; i < arr.length; i++) {
            hash += (hash << 5) + arr[i];
        }
        return hash;
    }

}