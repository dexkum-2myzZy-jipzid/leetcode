class Solution {
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        var intervals = intervals
        intervals.sort { $0[0] < $1[0] }

        var res: [[Int]] = []
        for interval in intervals {
            if res.isEmpty || res.last![1] < interval[0] {
                res.append(interval)
            } else {
                res[res.count - 1][1] = max(res.last![1], interval[1])
            }
        }

        return res
    }
}
