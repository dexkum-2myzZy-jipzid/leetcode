class Solution {
    func findBuildings(_ heights: [Int]) -> [Int] {
        // scan backforward, store highest height, compare it
        // if lower than it, so no ocean view, if higher than it, has ocean view
        let n = heights.count
        var res: [Int] = []

        var height = 0
        for i in stride(from: n - 1, to: -1, by: -1) {
            if heights[i] > height {
                res.append(i)
                height = heights[i]
            }
        }

        res.reverse()

        return res
    }
}

// monotonic stack solution, support dynamic add building
class Solution {
    func findBuildings(_ heights: [Int]) -> [Int] {
        // monotonic stack: decreasing order
        // scan forward, if heights[i] > last element in stack, stack pop

        let n = heights.count
        var stack: [Int] = []

        for i in 0 ..< n {
            while let last = stack.last, heights[i] >= heights[last] {
                stack.removeLast()
            }
            stack.append(i)
        }

        return stack
    }
}
