class Solution {
    func simplifyPath(_ path: String) -> String {
        let arr = path.split(separator: "/").filter { $0 != "" }

        var stack: [String] = []

        for e in arr {
            if e == ".." {
                stack.popLast()
            } else if e != "." {
                stack.append(String(e))
            }
        }

        // print(stack)

        return "/" + stack.joined(separator: "/")
    }
}
