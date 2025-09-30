class Solution {
    func wordBreak(_ s: String, _ wordDict: [String]) -> Bool {
        // dp[i] represent s[0..i] can be segmented into dic or not
        let chs = Array(s)
        let n = chs.count
        let wordSet = Set(wordDict)

        var dp = Array(repeating: false, count: n + 1)

        // init dp, "" string
        dp[0] = true

        for right in 1 ... n {
            for word in wordDict {
                let len = word.count
                // cur word len > right
                if len > right { continue }

                let left = right - len
                if !dp[left] { continue }

                let subStr = String(chs[left ..< right])
                if word == subStr {
                    dp[right] = true
                    break
                }
            }
        }

        return dp[n]
    }
}
