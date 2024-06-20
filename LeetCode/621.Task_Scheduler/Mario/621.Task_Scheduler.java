class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] counter = new int[128];
        for (char task : tasks) {
            counter[task] += 1;
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for (int i = 0; i < 128; i++) {
            int count = counter[i];
            if (count > 0) {
                pq.offer(count);
            }
        }

        int result = 0;
        while (!pq.isEmpty()) {
            int cycle = n + 1;
            List<Integer> store = new ArrayList<>();
            int task = 0;
            while (cycle > 0 && !pq.isEmpty()) {
                int freq = pq.poll();
                if (freq > 0) {
                    freq -= 1;
                    if (freq > 0)
                        store.add(freq);
                }
                task += 1;
                cycle -= 1;
            }

            store.forEach(pq::offer);
            result += pq.isEmpty() ? task : n + 1;
        }

        return result;
    }
}

// better solution - time: O(n)
class Solution {
    // A B _
    // A B _
    // A B
    public int leastInterval(char[] tasks, int n) {
        // counter task num
        int[] counter = new int[26];
        for (char c : tasks) {
            counter[c - 'A'] += 1;
        }

        Arrays.sort(counter);

        int maxFreq = counter[25];
        int idleNum = (maxFreq - 1) * n;

        for (int i = 24; i >= 0; i--) {
            idleNum -= Math.min(maxFreq - 1, counter[i]);
            if (idleNum < 0) {
                idleNum = 0;
                break;
            }
        }

        return tasks.length + idleNum;
    }
}