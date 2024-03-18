class Solution {
    public int minimumDeletions(String word, int k) {
        int[] counter = new int[26];
        for (char c : word.toCharArray()) {
            counter[c - 'a'] += 1;
        }

        Arrays.sort(counter);

        int maxSave = 0;
        for (int i = 0; i < 26; i++) {
            if (counter[i] == 0)
                continue;
            int sum = counter[i];
            for (int j = i + 1; j < 26; j++) {
                sum += Math.min(counter[i] + k, counter[j]);
            }
            maxSave = Math.max(maxSave, sum);
        }
        return word.length() - maxSave;
    }
}