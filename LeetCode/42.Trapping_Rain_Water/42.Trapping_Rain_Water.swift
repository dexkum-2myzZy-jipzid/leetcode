class Solution {
    func trap(_ height: [Int]) -> Int {
        // monotonic stack decreasing order
        var stack: [Int] = []
        var res = 0

        for (i, h) in height.enumerated() {
            while let last = stack.last, height[last] < h {
                let bottom = height[stack.removeLast()]
                if let left = stack.last {
                    let width = i - left - 1
                    let curHeight = min(h, height[left]) - bottom
                    let area = width * curHeight
                    res += area
                }
            }

            stack.append(i)
        }

        return res
    }
}
