class WordDistance {

    Map<String, List<Integer>> indexMap;

    public WordDistance(String[] wordsDict) {
        indexMap = new HashMap<>();
        for (int i = 0; i < wordsDict.length; i++) {
            String word = wordsDict[i];
            List<Integer> list = indexMap.getOrDefault(word, new ArrayList<Integer>());
            list.add(i);
            indexMap.put(word, list);
        }
    }

    public int shortest(String word1, String word2) {
        List<Integer> list1 = indexMap.get(word1);
        List<Integer> list2 = indexMap.get(word2);

        int res = Integer.MAX_VALUE;
        int i = 0, j = 0;
        while (i < list1.size() && j < list2.size()) {
            int index1 = list1.get(i);
            int index2 = list2.get(j);
            if (index1 < index2) {
                res = Math.min(res, index2 - index1);
                i += 1;
            } else {
                res = Math.min(res, index1 - index2);
                j += 1;
            }
        }
        return res;
    }
}

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance obj = new WordDistance(wordsDict);
 * int param_1 = obj.shortest(word1,word2);
 */