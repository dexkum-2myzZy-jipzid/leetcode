class Solution {
    struct Point: Comparable {
        let dis: Int
        let idx: Int

        init(_ dis: Int, _ idx: Int) {
            self.dis = dis
            self.idx = idx
        }

        static func < (lhs: Point, rhs: Point) -> Bool { lhs.dis < rhs.dis }
        static func == (lhs: Point, rhs: Point) -> Bool { lhs.dis == rhs.dis }
    }

    func kClosest(_ points: [[Int]], _ k: Int) -> [[Int]] {
        var heap = Heap<Point>()

        for (i, point) in points.enumerated() {
            let dis = point[0] * point[0] + point[1] * point[1]
            heap.insert(Point(dis, i))
            if heap.count > k {
                heap.popMax()
            }
        }

        var res: [[Int]] = []
        for p in heap.unordered {
            res.append(points[p.idx])
        }

        return res
    }
}
