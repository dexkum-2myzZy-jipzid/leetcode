class Solution {
    func numFriendRequests(_ ages: [Int]) -> Int {
        // x -> y send a request:
        // y > 0.5 * x + 7 && y <= x && (y <= 100 or x >= 100)
        var buckets = Array(repeating: 0, count: 121)

        for age in ages {
            buckets[age] += 1
        }

        var prefix: [Int] = Array(repeating: 0, count: 121)
        for i in 1 ... 120 {
            prefix[i] = prefix[i - 1] + buckets[i]
        }

        var res = 0
        for x in 15 ... 120 {
            // get x count
            let xCount = buckets[x]
            if xCount == 0 { continue }
            // get y count
            let left = x / 2 + 7, right = x
            if left >= right { continue }
            let yCount = prefix[right] - prefix[left]
            res += buckets[x] * (yCount - 1) // exclude itself
        }

        return res
    }
}
