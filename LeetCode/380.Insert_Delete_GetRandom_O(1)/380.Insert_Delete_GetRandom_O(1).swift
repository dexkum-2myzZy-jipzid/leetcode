class RandomizedSet {
    var dic: [Int: Int] = [:]
    var arr: [Int] = []

    init() {}

    func insert(_ val: Int) -> Bool {
        if let i = dic[val] { return false }
        let idx = arr.count
        arr.append(val)
        dic[val] = idx
        return true
    }

    func remove(_ val: Int) -> Bool {
        guard let i = dic[val] else { return false }
        let lastIdx = arr.count - 1
        if i != lastIdx {
            let lastVal = arr[lastIdx]
            arr[i] = lastVal
            dic[lastVal] = i
        }

        arr.removeLast()
        dic[val] = nil
        return true
    }

    func getRandom() -> Int {
        let idx = Int.random(in: 0 ..< arr.count)
        return arr[idx]
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet()
 * let ret_1: Bool = obj.insert(val)
 * let ret_2: Bool = obj.remove(val)
 * let ret_3: Int = obj.getRandom()
 */
