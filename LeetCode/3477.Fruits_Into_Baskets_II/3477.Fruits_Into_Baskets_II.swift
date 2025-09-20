// TC:O(n**2)
class Solution {
    func numOfUnplacedFruits(_ fruits: [Int], _ baskets: [Int]) -> Int {
        // return type that remain unplaced
        let n = fruits.count
        var baskets = baskets

        for f in fruits {
            for (i, b) in baskets.enumerated() {
                if b >= f {
                    baskets[i] = 0
                    break
                }
            }
        }

        return baskets.filter { $0 > 0 }.count
    }
}

// segment tree
