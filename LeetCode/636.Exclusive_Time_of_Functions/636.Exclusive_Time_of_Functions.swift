class Solution {
    func exclusiveTime(_ n: Int, _ logs: [String]) -> [Int] {
        var res = Array(repeating: 0, count: n)
        var stack: [Int] = []
        var prev_time = 0

        for log in logs {
            let parts = log.split(separator: ":")
            if let id = Int(parts[0]), let time = Int(parts[2]) {
                let type = parts[1]
                if type == "start" {
                    if let cur = stack.last {
                        res[cur] += time - prev_time
                    }
                    prev_time = time
                    stack.append(id)
                } else {
                    res[stack.last!] += time - prev_time + 1
                    prev_time = time + 1
                    stack.removeLast()
                }
            }
        }

        return res
    }
}
