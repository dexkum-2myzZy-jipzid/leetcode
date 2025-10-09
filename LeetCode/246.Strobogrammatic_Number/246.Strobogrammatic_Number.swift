class Solution {
    func isStrobogrammatic(_ num: String) -> Bool {
        // 1 = > 1 6, 8, 9 0
        var arr: [Character] = []
        let stroMap: [Character: Character] = [
            "1": "1", "6": "9", "8": "8",
            "9": "6", "0": "0",
        ]

        for ch in num {
            if let map = stroMap[ch] {
                arr.append(map)
            } else {
                return false
            }
        }

        return String(arr.reversed()) == num
    }
}
