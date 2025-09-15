# Swift LeetCode Cheatsheet

在 LeetCode 刷题时，Swift 和 Python 有很多不同的地方，这里整理一份常用速查表，方便快速切换思路。

---

## 1. 容器与数据结构

### 数组 (Array)

- **索引安全**：越界会崩溃。
- 常见操作：
  ```swift
  var arr = [1, 2, 3]
  arr.append(4)
  arr.removeLast()
  arr.popLast() // 返回 Optional
  ```
- **BFS 优化**：用 `head` 指针代替 `removeFirst()`。

### 双端队列 (Deque)

- 需要 `swift-collections`：
  ```swift
  import Collections
  var dq = Deque([1,2,3])
  dq.popFirst()
  dq.popLast()
  dq.append(4)
  dq.prepend(0)
  ```

### 集合 (Set)

```swift
var s: Set<Int> = [1, 2, 3]
if s.contains(2) { ... }
```

### 字典 (Dictionary)

- 查询结果是 Optional：
  ```swift
  var dic = ["a": 1, "b": 2]
  if let val = dic["a"] {
      print(val)
  }
  ```

---

## 2. 可选值 (Optionals)

### 解包方式

```swift
if let val = dic["key"] {
    // 安全解包
}
```

### 强制解包

```swift
let x: Int? = 5
print(x!)  // 若为 nil 会崩溃
```

刷题常见：字典取值、`popLast()` 结果都需要解包。

---

## 3. 字符串处理

- Swift 的 `String` 索引不是 Int：

  ```swift
  let s = "leetcode"
  let first = s[s.startIndex]
  ```

- 常见写法：

  ```swift
  let arr = Array(s)       // 转 [Character]
  let substr = s.prefix(3) // "lee"
  let idx = s.index(s.startIndex, offsetBy: 3)
  let char = s[idx]
  ```

---

## 4. 循环与遍历

- 带下标：

  ```swift
  for (i, val) in nums.enumerated() {
      ...
  }
  ```

- 范围循环：

  ```swift
  for i in 0..<n { }
  for i in 0...n { }
  ```

---

## 5. 函数与闭包

- 明确写返回类型：

  ```swift
  func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
      return [0,1]
  }
  ```

- 高阶函数：

  ```swift
  nums.map { $0 * 2 }
  nums.filter { $0 > 0 }
  nums.reduce(0, +)
  ```

---

## 6. 其他差异

- **堆 (PriorityQueue)**：没有内置，需要自己实现。
- **不可变默认**：`let` 是常量，`var` 才能修改。
- **值类型**：数组、字典、集合是值类型，拷贝时有性能差异。

---

## 7. Python vs Swift 对照表

| 场景    | Python                              | Swift                                                        |
| ----- | ----------------------------------- | ------------------------------------------------------------ |
| 队列    | `dq = deque([1,2,3]); dq.popleft()` | `import Collections; var dq = Deque([1,2,3]); dq.popFirst()` |
| 哈希表取值 | `if key in dic:`                    | `if let val = dic[key] { }`                                  |
| 字符串索引 | `s[0]`                              | `Array(s)[0]` 或 `s[s.startIndex]`                            |
| 遍历带下标 | `for i, v in enumerate(nums):`      | `for (i, v) in nums.enumerated()`                            |
| 范围循环  | `for i in range(n):`                | `for i in 0..<n`                                             |
| 堆     | `heapq.heappush(pq, x)`             | 自建 `Heap`                                                    |

---

✅ 这份速查表覆盖了 Swift 刷 LeetCode 常用的表达方式和坑点。

