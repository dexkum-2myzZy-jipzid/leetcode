class Solution {
    func lengthOfLIS(_ nums: [Int]) -> Int {
        var arr: [Int] = []

        func binarySearchLeft(_ target: Int) -> Int {
            var l = 0, r = arr.count
            while l < r {
                let mid = (l + r) >> 1
                if arr[mid] < target {
                    l = mid + 1
                } else {
                    r = mid
                }
            }
            return l
        }

        for num in nums {
            let idx = binarySearchLeft(num)
            if idx == arr.count {
                arr.append(num)
            } else {
                arr[idx] = num
            }
        }

        return arr.count
    }
}
