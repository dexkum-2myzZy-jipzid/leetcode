class Solution {
    func numRabbits(_ answers: [Int]) -> Int {
        // cnt = answers[i], cnt + 1
        var counter: [Int: Int] = [:]

        for cnt in answers {
            counter[cnt + 1, default: 0] += 1
        }

        // 1, 1, 1, first two 1 is pair, (3+2-1) / 2 = 2
        // 2 pair, 1 pairs has 2 rabbits, 2 * 2
        var res = 0
        // k is group isze, v : how many answers this ize
        for (k, v) in counter {
            let cnt = (v + k - 1) / k
            res += cnt * k
        }

        return res
    }
}
