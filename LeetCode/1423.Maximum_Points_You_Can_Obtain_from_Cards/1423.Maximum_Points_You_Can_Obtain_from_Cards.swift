// prefix sum
class Solution {
    func maxScore(_ cardPoints: [Int], _ k: Int) -> Int {
        // take from beginning or end, take k cards
        var pre = [0]
        for p in cardPoints {
            if let last = pre.last {
                pre.append(last + p)
            }
        }

        let n = pre.count

        var res = 0
        // start means take how many cards from the beginning
        for start in 0 ... k {
            let end = k - start
            let startSum = pre[start]
            let endSum = pre[n - 1] - pre[n - 1 - end]
            res = max(res, startSum + endSum)
        }

        return res
    }
}

// sliding window
class Solution {
    func maxScore(_ cardPoints: [Int], _ k: Int) -> Int {
        let n = cardPoints.count, sum = cardPoints.reduce(0, +)
        var l = 0, wind = 0, res = 0
        let windLen = n - k

        for (r, p) in cardPoints.enumerated() {
            wind += p
            while l <= r && r - l + 1 > windLen {
                wind -= cardPoints[l]
                l += 1
            }

            if r - l + 1 == windLen {
                res = max(sum - wind, res)
            }
        }

        return res
    }
}
