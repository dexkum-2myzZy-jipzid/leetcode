class Solution {
    func calculate(_ s: String) -> Int {
        // non-negative int
        let chars = Array(s) + ["#"]
        var lastOp: Character = "+"
        var last = 0, num = 0
        var res = 0

        for ch in chars {
            if let d = ch.wholeNumberValue {
                num = num * 10 + d
                continue
            }
            if ch == " " { continue }

            print("before:\tlastOp:\(lastOp)\tlast:\(last)\tnum:\(num)\t\tres:\(res)")

            switch lastOp {
            case "+":
                res += last
                last = num
            case "-":
                res += last
                last = -num
            case "*":
                last = last * num
            case "/":
                last = last / num
            default:
                break
            }

            lastOp = ch
            num = 0
            print("after:\tlastOp:\(lastOp)\tlast:\(last)\tnum:\(num)\t\tres:\(res)\n")
        }

        return res + last
    }
}

class Solution {
    func calculate(_ s: String) -> Int {
        // stack, lastOp
        var stack: [Int] = []
        var lastOp: Character = "+"
        var num = 0

        let chars = Array(s) + ["#"]

        for ch in chars {
            if let d = ch.wholeNumberValue {
                num = num * 10 + d
            } else {
                if ch == " " { continue }

                switch lastOp {
                case "+": stack.append(num)
                case "-": stack.append(-num)
                case "*": stack.append(stack.removeLast() * num)
                case "/": stack.append(stack.removeLast() / num)
                default: break
                }
                lastOp = ch
                num = 0
            }
        }

        return stack.reduce(0, +)
    }
}
