class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        guard strs.count >= 2 else { return strs[0] }

        var prefix = strs[0]
        for i in 1 ..< strs.count {
            let curr = strs[i]
            while !curr.hasPrefix(prefix) {
                if prefix.isEmpty { return "" }
                prefix.removeLast()
            }
            if prefix.isEmpty { return "" }
        }

        return prefix
    }
}
