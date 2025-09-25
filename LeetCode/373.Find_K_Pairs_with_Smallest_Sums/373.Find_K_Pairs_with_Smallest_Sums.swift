struct Pair: Comparable {
    let num1: Int, num2: Int, idx1: Int, idx2: Int

    static func < (_ lhs: Pair, _ rhs: Pair) -> Bool {
        return lhs.num1 + lhs.num2 < rhs.num1 + rhs.num2
    }
}

private struct Indices: Hashable {
    let i: Int, j: Int
}

class Solution {
    func kSmallestPairs(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> [[Int]] {
        var heap = Heap<Pair>()
        heap.insert(Pair(num1: nums1[0], num2: nums2[0], idx1: 0, idx2: 0))
        var res: [[Int]] = []
        var seen: Set<Indices> = [Indices(i: 0, j: 0)]

        while res.count < k, let top = heap.popMin() {
            let (num1, num2, idx1, idx2) = (top.num1, top.num2, top.idx1, top.idx2)

            res.append([num1, num2])

            if idx1 + 1 < nums1.count {
                let nxt = Indices(i: idx1 + 1, j: idx2)
                if !seen.contains(nxt) {
                    seen.insert(nxt)
                    heap.insert(Pair(num1: nums1[idx1 + 1], num2: nums2[idx2], idx1: idx1 + 1, idx2: idx2))
                }
            }
            if idx2 + 1 < nums2.count {
                let nxt = Indices(i: idx1, j: idx2 + 1)
                if !seen.contains(Indices(i: idx1, j: idx2 + 1)) {
                    seen.insert(Indices(i: idx1, j: idx2 + 1))
                    heap.insert(Pair(num1: nums1[idx1], num2: nums2[idx2 + 1], idx1: idx1, idx2: idx2 + 1))
                }
            }
        }

        return res
    }
}
