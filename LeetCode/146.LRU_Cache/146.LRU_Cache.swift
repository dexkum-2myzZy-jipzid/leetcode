
class LRUCache {
    private class Node {
        let key: Int
        var val: Int
        var prev: Node?
        var next: Node?

        init(_ key: Int, _ val: Int) {
            self.key = key
            self.val = val
        }
    }

    private var dic: [Int: Node] = [:]
    private var capacity: Int
    private var size: Int = 0
    private let head: Node = .init(-1, -1)
    private let tail: Node = .init(-2, -2)

    init(_ capacity: Int) {
        self.capacity = capacity
        head.next = tail
        tail.prev = head
    }

    func get(_ key: Int) -> Int {
        guard let node = dic[key] else { return -1 }
        removeNode(node)
        addToHead(node)
        return node.val
    }

    func put(_ key: Int, _ value: Int) {
        // get node from dic
        if let node = dic[key] {
            node.val = value
            removeNode(node)
            addToHead(node)
            return
        }

        if size < capacity {
            size += 1
        } else {
            if let remove = tail.prev {
                removeNode(remove)
                dic[remove.key] = nil
            }
        }
        let newNode = Node(key, value)
        addToHead(newNode)
        dic[key] = newNode
    }

    // basic operation to Linked List
    // remove node
    private func removeNode(_ node: Node) {
        if let prev = node.prev, let next = node.next {
            prev.next = next
            next.prev = prev
        }
        node.next = nil
        node.prev = nil
    }

    // add to head
    private func addToHead(_ node: Node) {
        let prev = head
        if let next = head.next {
            prev.next = node
            node.prev = prev
            next.prev = node
            node.next = next
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache(capacity)
 * let ret_1: Int = obj.get(key)
 * obj.put(key, value)
 */
