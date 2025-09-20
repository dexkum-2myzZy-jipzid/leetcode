
class SparseVector {
    private let entries: [(Int, Int)]
    // array:[(index, value)] value != 0
    init(_ nums: [Int]) {
        var tmp: [(Int, Int)] = []
        for (i, num) in nums.enumerated() {
            if num != 0 {
                tmp.append((i, num))
            }
        }
        entries = tmp
    }

    // Return the dotProduct of two sparse vectors
    func dotProduct(_ vec: SparseVector) -> Int {
        var res = 0
        var i = 0, j = 0
        while i < entries.count && j < vec.entries.count {
            let (idx1, num1) = entries[i]
            let (idx2, num2) = vec.entries[j]

            if idx1 == idx2 {
                res += (num1 * num2)
                i += 1
                j += 1
            } else if idx1 < idx2 {
                i += 1
            } else {
                j += 1
            }
        }
        return res
    }
}

/**
 * Your SparseVector object will be instantiated and called as such:
 * let v1 = SparseVector(nums1)
 * let v2 = SparseVector(nums2)
 * let ans = v1.dotProduct(v2)
 */
