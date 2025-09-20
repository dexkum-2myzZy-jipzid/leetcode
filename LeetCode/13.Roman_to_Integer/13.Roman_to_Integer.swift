class Solution {
    func romanToInt(_ s: String) -> Int {
        func charToInt(_ char: Character) -> Int {
            switch char {
            case "I": return 1
            case "V": return 5
            case "X": return 10
            case "L": return 50
            case "C": return 100
            case "D": return 500
            case "M": return 1000
            default: return 0
            }
        }

        var prev = 0
        var res = 0

        for ch in s.reversed() {
            var num = charToInt(ch)
            if num < prev {
                res -= num
            } else {
                res += num
            }
            prev = num
        }

        return res
    }
}
