class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var freq: [Int: Int] = [:]
        for num in nums {
            freq[num, default: 0] += 1
        }

        let n = nums.count
        var buckets = Array(repeating: [Int](), count: n + 1)
        for (num, cnt) in freq {
            buckets[cnt].append(num)
        }

        // print(buckets)

        var res: [Int] = []
        res.reserveCapacity(k)
        var need = k
        for i in stride(from: n, through: 0, by: -1) {
            for e in buckets[i] {
                res.append(e)
                need -= 1
                if need == 0 {
                    return res
                }
            }
        }

        return res
    }
}

struct Pair: Comparable {
    let freq: Int
    let num: Int

    static func < (lhs: Pair, rhs: Pair) -> Bool {
        return (lhs.freq, lhs.num) < (rhs.freq, rhs.num)
    }
}

class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var freq: [Int: Int] = [:]
        for num in nums {
            freq[num, default: 0] += 1
        }

        var heap = Heap<Pair>()
        heap.reserveCapacity(k)
        for (num, f) in freq {
            heap.insert(Pair(freq: f, num: num))
            if heap.count > k {
                _ = heap.popMin()
            }
        }

        var res: [Int] = []
        for p in heap.unordered {
            res.append(p.num)
        }

        return res
    }
}
