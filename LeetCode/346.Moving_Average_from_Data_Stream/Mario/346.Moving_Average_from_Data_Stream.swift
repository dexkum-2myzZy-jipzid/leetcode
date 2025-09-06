
class MovingAverage {
    // hold all values
    private var arr: [Int]
    // how many num in arr
    private var count: Int = 0
    // the index of num which will be deleted
    private var index: Int = 0
    // the size of arr
    private var size: Int
    // sum of this arr
    private var sum: Int = 0

    init(_ size: Int) {
        self.size = size
        arr = Array(repeating: 0, count: size)
    }

    func next(_ val: Int) -> Double {
        if count == size {
            sum -= arr[index]
        } else {
            count += 1
        }
        sum += val
        arr[index] = val
        index = (index + 1) % size
        return Double(sum) / Double(count)
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * let obj = MovingAverage(size)
 * let ret_1: Double = obj.next(val)
 */
