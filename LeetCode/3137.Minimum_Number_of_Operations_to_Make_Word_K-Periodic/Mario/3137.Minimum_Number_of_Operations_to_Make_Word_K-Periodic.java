class Solution {
    public int minimumOperationsToMakeKPeriodic(String word, int k) {
        int maxCount = word.length() / k;
        Map<String, Integer> counter = new HashMap<>();

        int localCount = 0;
        for (int i = 0; i < maxCount; i++) {
            String subStr = word.substring(i * k, (i + 1) * k);
            int count = counter.getOrDefault(subStr, 0) + 1;
            counter.put(subStr, count);
            localCount = Math.max(localCount, count);
        }

        return maxCount - localCount;
    }
}