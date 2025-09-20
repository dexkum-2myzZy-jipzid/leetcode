class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();
        int l = newInterval[0], r = newInterval[1];
        boolean merge = false;
        for (int[] i : intervals) {
            if (r < i[0]) {
                if (!merge) {
                    res.add(new int[] { l, r });
                    merge = true;
                }
                res.add(i);
            } else if (i[1] < l) {
                res.add(i);
            } else {
                l = Math.min(i[0], l);
                r = Math.max(i[1], r);
            }
        }

        if (!merge) {
            res.add(new int[] { l, r });
        }

        return res.toArray(new int[res.size()][]);
    }
}