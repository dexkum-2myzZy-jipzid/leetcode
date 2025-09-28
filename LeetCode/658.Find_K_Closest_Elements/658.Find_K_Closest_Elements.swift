class Solution {
    func findClosestElements(_ arr: [Int], _ k: Int, _ x: Int) -> [Int] {
        // sorted arr int
        var lst: [(Int, Int)] = []
        for num in arr {
            lst.append((abs(num - x), num))
        }

        lst.sort { ($0.0, $0.1) < ($1.0, $1.1) }

        let res = Array(lst.map { $0.1 }.prefix(k))

        return res.sorted()
    }
}

// Binary Search
class Solution {
    func findClosestElements(_ arr: [Int], _ k: Int, _ x: Int) -> [Int] {
        let n = arr.count
        guard n >= k else { return [] }

        var l = 0, r = n - k

        while l < r {
            let mid = (l + r) >> 1

            let leftDis = x - arr[mid]
            let rightDis = arr[mid + k] - x

            if leftDis > rightDis {
                l = mid + 1
            } else {
                r = mid
            }
        }

        return Array(arr[l ..< l + k])
    }
}
