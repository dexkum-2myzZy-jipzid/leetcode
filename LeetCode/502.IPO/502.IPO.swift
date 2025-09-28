class Solution {
    func findMaximizedCapital(_ k: Int, _ w: Int, _ profits: [Int], _ capital: [Int]) -> Int {
        // find which projects init capital <= w,
        // so start most profit project in these projects
        let n = profits.count

        var projects = zip(capital, profits).sorted { $0.0 < $1.0 }
        var i = 0

        var heap = Heap<Int>()
        var cur = w, count = 0

        while count < k {
            while i < n && cur >= projects[i].0 {
                heap.insert(projects[i].1)
                i += 1
            }

            if let max = heap.popMax() {
                cur += max
                count += 1
            } else {
                break
            }
        }

        return cur
    }
}
