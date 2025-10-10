class UnionFind {
    private var parent: [Int]
    private var size: [Int]

    init(_ n: Int) {
        parent = Array(0 ..< n)
        size = Array(repeating: 1, count: n)
    }

    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    func union(_ x: Int, _ y: Int) -> Bool {
        var rx = find(x), ry = find(y)
        guard rx != ry else { return false }

        if size[ry] > size[rx] { swap(&rx, &ry) }
        parent[ry] = rx
        size[rx] += size[ry]
        return true
    }

    func connected(_ x: Int, _ y: Int) -> Bool {
        return find(x) == find(y)
    }
}
