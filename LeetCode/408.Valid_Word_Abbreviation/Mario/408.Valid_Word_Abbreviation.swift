class Solution {
    func validWordAbbreviation(_ word: String, _ abbr: String) -> Bool {
        let wordArr = Array(word), abbrArr = Array(abbr)
        let n = wordArr.count, m = abbrArr.count
        var i = 0, j = 0

        while i < n && j < m {
            if wordArr[i] == abbrArr[j] {
                i += 1
                j += 1
            } else {
                if abbrArr[j].isNumber && abbrArr[j] != "0" {
                    var num = 0
                    while j < m && abbrArr[j].isNumber {
                        num = num * 10 + Int(String(abbrArr[j]))!
                        j += 1
                    }
                    i += num
                } else {
                    return false
                }
            }
        }

        return i == n && j == m
    }
}
