class Solution {
    public int minimumDeletions(String word, int k) {
        Map<Character, Integer> counter = new HashMap<>();

        for (char ch : word.toCharArray()) {
            counter.put(ch, counter.getOrDefault(ch, 0) + 1);
        }

        List<Integer> list = new ArrayList<>();
        for (Integer val : counter.values()) {
            list.add(val);
        }

        Collections.sort(list);
        // System.out.println(list);
        int n = list.size();

        return helper(list, 0, n - 1, k, 0);
    }

    private int helper(List<Integer> list, int i, int j, int k, int count) {
        int left = list.get(i), right = list.get(j);
        if (right - left <= k) {
            return count;
        }
        int diff = right - left - k;
        return Math.min(helper(list, i, j - 1, k, count + diff), helper(list, i + 1, j, k, count + left));
    }
}