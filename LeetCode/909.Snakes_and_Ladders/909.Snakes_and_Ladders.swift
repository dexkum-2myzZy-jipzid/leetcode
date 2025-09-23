class Solution {
    func snakesAndLadders(_ board: [[Int]]) -> Int {
        let n = board.count

        // 1 -> (n-1, 0)
        func indexToPoint(_ index: Int) -> (Int, Int) {
            let zeroBase = index - 1
            let rowFromBottom = zeroBase / n + 1
            let row = n - rowFromBottom
            //
            let col = rowFromBottom & 1 == 1 ? zeroBase % n : (n - 1 - zeroBase % n)

            return (row, col)
        }

        // print(indexToPoint(1))
        // print(indexToPoint(15))
        var q = [1], head = 0, step = 0
        var seen: Set<Int> = [1]

        while head < q.count {
            let size = q.count - head

            for _ in 0 ..< size {
                let curr = q[head]
                head += 1

                if curr == n * n {
                    return step
                }

                for add in 1 ... 6 {
                    var next = curr + add
                    if next > n * n { break }

                    let (r, c) = indexToPoint(next)
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
