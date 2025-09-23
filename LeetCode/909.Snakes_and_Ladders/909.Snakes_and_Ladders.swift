class Solution {
    func snakesAndLadders(_ board: [[Int]]) -> Int {
        // if has a snake or ladder, move to dest
        // [curr + 1, min(curr + 6, n2)]

        let n = board.count

        // 1 -> (n-1, 0) 15 -> (n-3, 3) n = 6
        func toPoint(_ label: Int) -> (Int, Int) {
            let zeroBase = label - 1
            let r = n - 1 - (zeroBase / n)
            // get col
            let rowFromBottom = zeroBase / n + 1
            // left -> right
            let c = rowFromBottom & 1 == 1 ? zeroBase % n : (n - 1 - zeroBase % n)
            return (r, c)
        }

        let target = n * n
        var q = [1]
        var seen: Set<Int> = [1]
        var head = 0, step = 0

        while head < q.count {
            let size = q.count - head

            for _ in 0 ..< size {
                let label = q[head]
                head += 1

                if label == target {
                    return step
                }

                for i in 1 ... 6 {
                    var next = label + i
                    if next > target { break }

                    let (r, c) = toPoint(next)
                    if board[r][c] != -1 {
                        next = board[r][c]
                    }

                    if !seen.contains(next) {
                        seen.insert(next)
                        q.append(next)
                    }
                }
            }
            step += 1
        }

        return -1
    }
}
