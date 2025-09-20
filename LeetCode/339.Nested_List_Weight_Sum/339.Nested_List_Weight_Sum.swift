/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public func isInteger() -> Bool
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     public func getInteger() -> Int
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public func setInteger(value: Int)
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public func add(elem: NestedInteger)
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     public func getList() -> [NestedInteger]
 * }
 */
// recusive
class Solution {
    func depthSum(_ nestedList: [NestedInteger]) -> Int {
        // int or list
        return dfs(nestedList, 1)
    }

    func dfs(_ lst: [NestedInteger], _ depth: Int) -> Int {
        var res = 0
        for e in lst {
            if e.isInteger() {
                res += e.getInteger() * depth
            } else {
                res += dfs(e.getList(), depth + 1)
            }
        }
        return res
    }
}

// queue
class Solution {
    func depthSum(_ nestedList: [NestedInteger]) -> Int {
        var q: [NestedInteger] = nestedList
        var head = 0, depth = 1
        var res = 0
        while head < q.count {
            let size = q.count - head
            for _ in 0 ..< size {
                let element = q[head]
                head += 1
                if element.isInteger() {
                    res += element.getInteger() * depth
                } else {
                    let lst = element.getList()
                    q.append(contentsOf: lst)
                }
            }
            depth += 1
        }
        return res
    }
}

class Solution {
    func depthSum(_ nestedList: [NestedInteger]) -> Int {
        var q: [(NestedInteger, Int)] = []
        for e in nestedList {
            q.append((e, 1))
        }
        var head = 0
        var res = 0
        while head < q.count {
            let (e, depth) = q[head]
            head += 1
            if e.isInteger() {
                res += e.getInteger() * depth
            } else {
                let lst = e.getList()
                for sub in lst {
                    q.append((sub, depth + 1))
                }
            }
        }
        return res
    }
}
