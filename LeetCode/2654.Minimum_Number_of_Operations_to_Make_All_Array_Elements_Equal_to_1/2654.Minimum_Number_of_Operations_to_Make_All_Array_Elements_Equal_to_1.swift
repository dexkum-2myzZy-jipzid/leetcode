class Solution {
    func gcd(_ a: Int, _ b: Int) -> Int {
        return b == 0 ? a : gcd(b, a % b)
    }

    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        guard n > 1 else { return -1 }
        var ones = 0, allgcd = nums[0]

        for i in 0 ..< n {
            ones += (nums[i] == 1 ? 1 : 0)
            allgcd = gcd(allgcd, nums[i])
        }

        if allgcd != 1 { return -1 }
        if ones > 0 { return n - ones }

        var minOp = Int.max

        for i in 0 ..< n {
            var curgcd = nums[i], op = 0
            for j in (i + 1) ..< n {
                curgcd = gcd(curgcd, nums[j])
                op += 1
                if curgcd == 1 { break }
            }

            if curgcd == 1 { minOp = min(minOp, op) }
            if minOp == 1 { break }
        }

        return n - 1 + minOp
    }
}
