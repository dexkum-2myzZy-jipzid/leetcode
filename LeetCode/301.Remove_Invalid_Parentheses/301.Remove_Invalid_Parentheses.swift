// dfs
class Solution {
    func removeInvalidParentheses(_ s: String) -> [String] {
        // remove invalide P
        let chs = Array(s)
        let n = chs.count
        // 1. get min removal count
        var stack: [Int] = [], minRemoval = 0
        for (i, ch) in chs.enumerated() {
            if ch == "(" {
                stack.append(i)
            } else if ch == ")" {
                if stack.isEmpty {
                    minRemoval += 1
                } else {
                    stack.removeLast()
                }
            }
        }
        minRemoval += stack.count

        var res = Set<String>()
        // 2. dfs i, open, close, removeCnt
        // open >= close
        func dfs(_ i: Int, _ o: Int, _ c: Int, _ remove: Int, _ path: [Character]) {
            if o < c { return }
            if i == n {
                if o == c, remove == 0 { res.insert(String(path)) }
                return
            }
            if remove < 0 { return }

            let curr = chs[i]
            if curr == "(" || curr == ")" {
                // take it
                if curr == "(" {
                    dfs(i + 1, o + 1, c, remove, path + [curr])
                } else {
                    dfs(i + 1, o, c + 1, remove, path + [curr])
                }
                // not take
                dfs(i + 1, o, c, remove - 1, path)
            } else {
                dfs(i + 1, o, c, remove, path + [curr])
            }
        }

        dfs(0, 0, 0, minRemoval, [])
        return Array(res)
    }
}

// bfs
class Solution {
    func removeInvalidParentheses(_ s: String) -> [String] {
        var q = [s], head = 0
        var res = Set<String>()
        var seen: Set<String> = [s]

        func isValid(_ chs: [Character]) -> Bool {
            var l = 0, r = 0
            for ch in chs {
                if ch == "(" {
                    l += 1
                } else if ch == ")" {
                    r += 1
                }
                if r > l { return false }
            }
            return l == r
        }

        while head < q.count {
            let size = q.count - head

            if !res.isEmpty {
                return Array(res)
            }

            for _ in 0 ..< size {
                let cur = q[head]
                var chs = Array(cur)
                head += 1

                if isValid(chs) {
                    res.insert(String(chs))
                }

                for i in 0 ..< chs.count {
                    let ch = chs[i]
                    if ch == "(" || ch == ")" {
                        chs.remove(at: i)
                        let nx = String(chs)
                        if !seen.contains(nx) {
                            seen.insert(nx)
                            q.append(nx)
                        }
                        chs.insert(ch, at: i)
                    }
                }
            }
        }

        return Array(res)
    }
}
