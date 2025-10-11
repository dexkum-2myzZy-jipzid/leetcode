// dfs
class Solution {
    func mincostTickets(_ days: [Int], _ costs: [Int]) -> Int {
        let n = days.count
        let (one, seven, thirty) = (costs[0], costs[1], costs[2])

        var memo: [Int: Int] = [:]

        func dfs(_ i: Int) -> Int {
            guard i < n else { return 0 }

            if let p = memo[i] {
                return p
            }

            // 1d, 7d, 30d
            let cur = days[i]

            let price1 = dfs(i + 1) + one
            var last = cur + 6
            let price2 = dfs(searchIdx(last)) + seven
            last = cur + 29
            let price3 = dfs(searchIdx(last)) + thirty

            let p = min(price1, price2, price3)
            memo[i] = p

            return p
        }

        func searchIdx(_ day: Int) -> Int {
            var l = 0, r = n
            while l < r {
                let m = (l + r) / 2
                if days[m] <= day {
                    l = m + 1
                } else {
                    r = m
                }
            }
            return l
        }

        return dfs(0)
    }
}

// dp
class Solution {
    func mincostTickets(_ days: [Int], _ costs: [Int]) -> Int {
        let n = days.count
        let (c1, c2, c3) = (costs[0], costs[1], costs[2])
        let last = days.last!

        var isTravel = Array(repeating: false, count: last + 1)
        for d in days {
            isTravel[d] = true
        }

        var dp = Array(repeating: 0, count: last + 1)

        for d in 1 ... last {
            if !isTravel[d] {
                dp[d] = dp[d - 1]
            } else {
                // 1 day pass
                let p1 = dp[max(0, d - 1)] + c1
                let p2 = dp[max(0, d - 7)] + c2
                let p3 = dp[max(0, d - 30)] + c3
                dp[d] = min(p1, p2, p3)
            }
        }

        return dp[last]
    }
}
