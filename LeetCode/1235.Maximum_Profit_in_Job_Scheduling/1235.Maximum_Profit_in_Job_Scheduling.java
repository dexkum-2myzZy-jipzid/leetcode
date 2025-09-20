class Solution {
    Map<Integer, Integer> map;

    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        // cache path result
        map = new HashMap<>();

        // build jobs
        int n = profit.length;
        List<Job> jobs = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            jobs.add(new Job(startTime[i], endTime[i], profit[i]));
        }

        // sort by startTime
        Collections.sort(jobs, (a, b) -> (a.startTime - b.startTime));

        // dfs
        return dfs(jobs, 0);
    }

    private int dfs(List<Job> jobs, int index) {
        if (index == jobs.size())
            return 0;
        if (map.containsKey(index)) {
            return map.get(index);
        }

        // not include index
        int result = dfs(jobs, index + 1);

        // include index
        int j = findNextIndex(jobs, index);
        result = Math.max(result, dfs(jobs, j) + jobs.get(index).profit);
        map.put(index, result);

        return result;
    }

    private int findNextIndex(List<Job> jobs, int index) {
        Job cur = jobs.get(index);
        int end = cur.endTime;

        int left = index, right = jobs.size() - 1;

        if (end > jobs.get(right).startTime) {
            return jobs.size();
        }

        while (left < right) {
            int mid = (left + right) / 2;
            if (jobs.get(mid).startTime < end) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}

class Job {
    public int startTime;
    public int endTime;
    public int profit;

    Job(int start, int end, int profit) {
        this.startTime = start;
        this.endTime = end;
        this.profit = profit;
    }
}
