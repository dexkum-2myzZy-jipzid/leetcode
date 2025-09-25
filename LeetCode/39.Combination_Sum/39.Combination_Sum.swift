class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        var cand = candidates
        cand.sort()
        let n = cand.count

        var res: [[Int]] = []
        var path: [Int] = []

        func backtrack(_ i: Int, _ sum: Int) {
            if sum >= target {
                if sum == target {
                    res.append(path)
                }
                return
            }

            for j in i ..< n {
                path.append(cand[j])
                backtrack(j, sum + cand[j])
                path.removeLast()
            }
        }

        backtrack(0, 0)

        return res
    }
}
