/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * public class Robot {
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     public func move() -> Bool {}
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     public func turnLeft() {}
 *     public func turnRight() {}
 *
 *     // Clean the current cell.
 *     public func clean() {}
 * }
 */

class Solution {
    struct Point: Hashable {
        let x, y: Int
    }

    func cleanRoom(_ robot: Robot) {
        func goBack() {
            robot.turnRight()
            robot.turnRight()
            _ = robot.move()
            robot.turnRight()
            robot.turnRight()
        }

        let dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        var seen = Set<Point>()

        func backtrack(_ x: Int, _ y: Int, _ dir: Int) {
            let cur = Point(x: x, y: y)
            seen.insert(cur)
            robot.clean()

            for i in 0 ..< 4 {
                let face = (dir + i) % 4
                let (dx, dy) = dirs[face]
                let nx = x + dx, ny = y + dy
                let next = Point(x: nx, y: ny)

                if !seen.contains(next), robot.move() {
                    backtrack(nx, ny, face)

                    goBack()
                }

                robot.turnRight()
            }
        }

        backtrack(0, 0, 0)
    }
}
