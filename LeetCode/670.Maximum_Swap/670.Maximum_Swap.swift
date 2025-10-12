class Solution {
    func maximumSwap(_ num: Int) -> Int {
        var chs = Array(String(num))
        let n = chs.count
        // backforwad scan,
        var indice = Array(repeating: -1, count: 10)
        var tmp = num, i = n - 1
        while tmp > 0 && i >= 0 {
            let digit = tmp % 10
            if indice[digit] == -1 {
                indice[digit] = i
            }
            i -= 1
            tmp /= 10
        }

        // forward
        var found = false, (a, b) = (-1, -1)
        for (i, ch) in chs.enumerated() {
            if let cur = Int(String(ch)) {
                // find digit is bigger cur, and indice is bigger than cur
                if cur == 9 {
                    continue // no one bigger than it
                } else {
                    for d in (0 ... 9).reversed() {
                        if d <= cur { break }

                        if indice[d] > i {
                            chs.swapAt(i, indice[d])
                            found = true
                            break
                        }
                    }
                }
                if found { break }
            }
        }

        return Int(String(chs))!
    }
}

class Solution {
    func maximumSwap(_ num: Int) -> Int {
        var digits = Array(String(num)).compactMap { $0.wholeNumberValue }
        // array index is digit, val is index
        var indice = Array(repeating: -1, count: 10)
        for (i, d) in digits.enumerated() {
            indice[d] = i
        }

        // find smaller num on the left side, then swap with biggest digit in right side
        for (i, d) in digits.enumerated() {
            if d == 9 { continue } // no digit bigger than 9
            for m in stride(from: 9, through: d + 1, by: -1) {
                let j = indice[m]
                if j > i {
                    digits.swapAt(i, j)
                    return toInt(digits)
                }
            }
        }

        return toInt(digits)
    }

    func toInt(_ digits: [Int]) -> Int {
        var res = 0
        for d in digits {
            res *= 10
            res += d
        }
        return res
    }
}
