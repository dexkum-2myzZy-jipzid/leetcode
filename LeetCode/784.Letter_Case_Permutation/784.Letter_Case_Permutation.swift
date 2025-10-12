class Solution {
    func letterCasePermutation(_ s: String) -> [String] {
        let chs = Array(s)
        let n = chs.count
        var res: [String] = []

        func backtrack(_ i: Int, _ path: [Character]) {
            if i == n {
                res.append(String(path))
                return
            }

            let cur = chs[i]
            if cur.isNumber {
                backtrack(i + 1, path + [cur])
            } else {
                // lowercase
                let lower = Character(cur.lowercased())
                backtrack(i + 1, path + [lower])

                // uppercase
                let upper = Character(cur.uppercased())
                backtrack(i + 1, path + [upper])
            }
        }

        backtrack(0, [])

        return res
    }
}
