class Solution {
    func sum(_ k: Int, _ i: Int, _ n: Int) -> Int {
        let lcnt = i, rcnt = n - 1 - i

        func sideSum(_ cnt: Int) -> Int {
            if cnt < k - 1 {
                return (k - 1 + k - cnt) * cnt / 2
            } else {
                return k * (k - 1) / 2 + cnt - (k - 1)
            }
        }

        return sideSum(lcnt) + sideSum(rcnt) + k
    }

    func maxValue(_ n: Int, _ index: Int, _ maxSum: Int) -> Int {
        // binary search
        var l = 1, r = maxSum + 1
        var res = 0
        while l < r {
            let mid = (l + r) >> 1
            if sum(mid, index, n) <= maxSum {
                l = mid + 1
                res = mid
            } else {
                r = mid
            }
        }

        return res
    }
}
