// heap
class Solution {
    func findKthLargest(_ nums: [Int], _ k: Int) -> Int {
        var heap = Heap<Int>()

        for num in nums {
            heap.insert(num)
            if heap.count > k {
                heap.popMin()
            }
        }

        return heap.popMin()!
    }
}

// quick select
class Solution {
    func findKthLargest(_ nums: [Int], _ k: Int) -> Int {
        var nums = nums

        var left = 0, right = nums.count - 1

        while true {
            let idx = partition(&nums, left, right)
            if idx + 1 == k {
                return nums[idx]
            } else if idx < k {
                left = idx + 1
            } else {
                right = idx - 1
            }
        }
    }
}

// decreasing nums
private func partition(_ nums: inout [Int], _ left: Int, _ right: Int) -> Int {
    let pivot = nums[right]
    var l = left

    for i in left ..< right {
        if nums[i] >= pivot {
            nums.swapAt(l, i)
            l += 1
        }
    }

    nums.swapAt(l, right)
    // print("nums:\(nums)\tpivot:\(pivot)\tl:\(l)")
    return l
}
