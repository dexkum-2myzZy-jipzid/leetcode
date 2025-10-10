class Solution {
    func generateParenthesis(_ n: Int) -> [String] {
        var res: [String] = []

        func dfs(_ l: Int, _ r: Int, _ path: [Character]) {
            guard l <= n, r <= n else { return }

            if l == n, r == n {
                res.append(String(path))
                return
            }

            // no l < r case
            if l > r {
                dfs(l + 1, r, path + ["("])
                dfs(l, r + 1, path + [")"])
            } else if l == r {
                dfs(l + 1, r, path + ["("])
            }
        }

        dfs(0, 0, [])
        return res
    }
}
