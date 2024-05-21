# Go CheatSheet

## String

Certainly! Here's a cheat sheet for manipulating strings in Go:

1. **Creating Strings**:

   - Declare and initialize: `str := "Hello, World!"`

2. **String Length**:

   - Get length: `length := len(str)`

3. **Accessing Characters**:

   - Get character at index: `char := str[index]`

4. **String Slicing**:

   - Extract substring: `substring := str[startIndex:endIndex]`

5. **Concatenation**:

   - Concatenate strings: `result := str1 + str2`
   - Use `fmt.Sprintf()`: `result := fmt.Sprintf("%s%s", str1, str2)`

6. **String Comparison**:

   - Compare equality: `isEqual := str1 == str2`
   - Case-insensitive comparison: `isEqual := strings.EqualFold(str1, str2)`

7. **Searching**:

   - Check substring presence: `isPresent := strings.Contains(str, substr)`
   - Find index of substring: `index := strings.Index(str, substr)`

8. **Replacing**:

   - Replace substring: `newStr := strings.Replace(str, oldSubstr, newSubstr, -1)`

9. **Trimming**:

   - Trim leading and trailing spaces: `trimmedStr := strings.TrimSpace(str)`

10. **Splitting**:

    - Split into substrings: `parts := strings.Split(str, delimiter)`

11. **Joining**:

    - Join substrings: `joinedStr := strings.Join(parts, separator)`

12. **Conversion**:

    - Convert to byte slice: `bytes := []byte(str)`
    - Convert to string: `str := string(bytes)`

13. **Formatting**:
    - Format with placeholders: `formattedStr := fmt.Sprintf("Value: %d", value)`
    - Format using `strings.Builder` for efficiency:
      ```go
      var builder strings.Builder
      builder.WriteString("Hello, ")
      builder.WriteString("World!")
      formattedStr := builder.String()
      ```

These are some common operations for manipulating strings in Go. Remember to import the `strings` package for functions related to string manipulation, and use `fmt` package for formatting strings.

## Slice

To manipulate arrays in Go, you can perform various operations such as accessing elements, modifying elements, and iterating over the array. Here are examples of how you can manipulate an array:

1. **Initializing an array**:

```go
var arr [5]int // Declare an array of integers with length 5
```

2. **Assigning values to elements**:

```go
arr := [5]int{1, 2, 3, 4, 5} // Initialize array with values
```

3. **Accessing elements**:

```go
arr := [5]int{1, 2, 3, 4, 5}
fmt.Println("Element at index 2:", arr[2]) // Output: 3
```

4. **Modifying elements**:

```go
arr := [5]int{1, 2, 3, 4, 5}
arr[2] = 10 // Modify the value at index 2 to 10
```

5. **Iterating over the array**:

```go
arr := [5]int{1, 2, 3, 4, 5}
for i := 0; i < len(arr); i++ {
    fmt.Println("Element at index", i, ":", arr[i])
}
```

6. **Iterating over the array using range**:

```go
arr := [5]int{1, 2, 3, 4, 5}
for index, value := range arr {
    fmt.Println("Element at index", index, ":", value)
}
```

7. **Getting the length of the array**:

```go
arr := [5]int{1, 2, 3, 4, 5}
length := len(arr) // length is 5
```

These are some basic operations you can perform on arrays in Go. Arrays have a fixed size and are suitable for situations where the size of the collection is known in advance. If you need a dynamically sized collection, consider using slices.

## Map

To manipulate a map in Go, you can perform various operations such as inserting, updating, deleting elements, and checking for the existence of keys. Here are examples of how you can manipulate a map:

1. **Inserting elements**:

```go
m := make(map[string]int)
m["apple"] = 10
m["banana"] = 5
```

2. **Updating elements**:

```go
m := make(map[string]int)
m["apple"] = 10
m["banana"] = 5

m["apple"] = 15 // Update the value for the key "apple"
```

3. **Deleting elements**:

```go
m := make(map[string]int)
m["apple"] = 10
m["banana"] = 5

delete(m, "apple") // Delete the element with key "apple"
```

4. **Checking if a key exists**:

```go
m := make(map[string]int)
m["apple"] = 10
m["banana"] = 5

value, exists := m["apple"]
if exists {
    fmt.Println("Value of 'apple' is:", value)
} else {
    fmt.Println("'apple' does not exist in the map")
}
```

These are some basic operations you can perform on a map in Go. Maps are versatile data structures that allow efficient storage and retrieval of key-value pairs.
