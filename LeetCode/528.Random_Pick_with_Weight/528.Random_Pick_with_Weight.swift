
class Solution {
    var prefix: [Int]
    let total: Int

    init(_ w: [Int]) {
        var run = 0
        prefix = w.map { e in
            run += e
            return run
        }
        total = run
    }

    func pickIndex() -> Int {
        let t = Int.random(in: 1 ... total)
        var l = 0, r = prefix.count
        while l < r {
            let m = l + (r - l) >> 1
            if prefix[m] < t {
                l = m + 1
            } else {
                r = m
            }
        }
        return l
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution(w)
 * let ret_1: Int = obj.pickIndex()
 */
