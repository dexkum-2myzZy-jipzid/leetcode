class Solution {
    func placeWordInCrossword(_ board: [[Character]], _ word: String) -> Bool {
        // scan row by row / col by col
        let m = board.count, n = board[0].count
        let chs = Array(word)
        let rchs = Array(word.reversed())

        let block: Character = "#", space: Character = " "

        func checkLine(_ line: [Character]) -> Bool {
            var slot: [Character] = []

            for i in 0 ... line.count {
                if i < line.count, line[i] != block {
                    slot.append(line[i])
                } else {
                    // check slot with chs
                    if compare(slot, chs) || compare(slot, rchs) { return true }
                    slot = []
                }
            }
            return false
        }

        func compare(_ slot: [Character], _ w: [Character]) -> Bool {
            guard slot.count == w.count else { return false }
            for (a, b) in zip(slot, w) {
                if a != space && a != b { return false }
            }
            return true
        }

        for r in board {
            if checkLine(r) { return true }
        }

        for i in 0 ..< n {
            var line: [Character] = []
            for j in 0 ..< m {
                line.append(board[j][i])
            }
            if checkLine(line) { return true }
        }

        return false
    }
}
