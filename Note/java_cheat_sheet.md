# Java CheatSheet



## Built-in data types

Here's a table summarizing the built-in data types in Java:

| Data Type | Size      | Min Value       | Max Value            | Use                                |
| --------- | --------- | --------------- | -------------------- | ---------------------------------- |
| Byte      | 8-bit     | -128            | 127                  | Very small integer values          |
| Short     | 16-bit    | -32,768         | 32,767               | Short integer values               |
| Int       | 32-bit    | -2^31           | 2^31-1               | General integer values             |
| Long      | 64-bit    | -2^63           | 2^63-1               | Large integer values               |
| Float     | 32-bit    | ~-3.4E38        | ~3.4E38              | Floating point numbers (precision) |
| Double    | 64-bit    | ~-1.7E308       | ~1.7E308             | Double precision floating points   |
| Boolean   | Not fixed | true/false      | true/false           | True or false conditions           |
| Char      | 16-bit    | '\u0000' (or 0) | '\uffff' (or 65,535) | Single Unicode characters          |



## String Usage

Here are some key points and common methods for `String` usage in Java:

1. **String Declaration and Initialization**:
   - `String str = "Hello World";` – Declares and initializes a string.
   - `String str = new String("Hello World");` – Another way to create a string.

2. **String Concatenation**:
   - `String fullName = firstName + " " + lastName;` – Combines strings.
   - `String fullName = "Hello, " + name + "!";` – Concatenates literals and variables.

3. **String Methods**:
   - `length()`: Returns the length of the string.
   - `charAt(int index)`: Returns the character at the specified index.
   - `substring(int beginIndex, int endIndex)`: Returns a substring.
   - `equals(String anotherString)`: Compares two strings for content equality.
   - `equalsIgnoreCase(String anotherString)`: Compares two strings, ignoring case.
   - `contains(CharSequence s)`: Checks if the string contains a sequence of characters.
   - `indexOf(String str)`: Returns the index of the first occurrence of the specified substring.
   - `toLowerCase()`: Converts all characters in the string to lower case.
   - `toUpperCase()`: Converts all characters in the string to upper case.
   - `trim()`: Removes whitespace from both ends of the string.
   - `replace(char oldChar, char newChar)`: Replaces all occurrences of a specified character.

4. **String Immutability**:
   - In Java, strings are immutable, meaning once a `String` object is created, its contents cannot be changed. Modifying a string actually creates a new string.

5. **String Comparison**:
   
   - Use `equals()` for content comparison.
   - Use `==` to check if two string references point to the same object.
   
6. **String Pool**:
   - Java maintains a special area in memory called the String Pool to store string literals. If a new string matches an existing one in the pool, the new string will reference the existing one to save memory.

7. **StringBuilder and StringBuffer**:
   - For strings that need to be modified frequently, `StringBuilder` (not synchronized) and `StringBuffer` (synchronized) are more efficient than using `String`.
   
     

### `==`  vs `equals`

For example:

- `String a = "Hello";`
- `String b = "Hello";`
- `String c = new String("Hello");`

In this case, `a == b` would return `true` because both `a` and `b` refer to the same string literal in the string pool. However, `a == c` would return `false` because `c` is created as a new `String` object, and it resides in a different memory location, even though it contains the same characters as `a`.



### Conversion between String and num

In Java, you can convert an `int` to a `String` using either the `String.valueOf()` method or the `Integer.toString()` method. Here's how you can do it:

Using `String.valueOf()` method:
```java
int num = 123;
String str = String.valueOf(num);
```

Using `Integer.toString()` method:
```java
int num = 123;
String str = Integer.toString(num);
```

Both methods will convert the `int` value `123` to the `String` value `"123"`. You can then use the resulting `String` object as needed in your program.



### Char

```java
char[] charArray = s.toCharArray();
```





### StringBuilder

Here's a table summarizing common `StringBuilder` methods and their usage in Java:

| Method                                    | Description                                                  | Example Usage                                                |
| ----------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `StringBuilder()`                         | Creates an empty `StringBuilder` with a default capacity.    | `StringBuilder sb = new StringBuilder();`                    |
| `StringBuilder(String str)`               | Creates a `StringBuilder` containing the specified string.   | `StringBuilder sb = new StringBuilder("Hello");`             |
| `append(...)`                             | Appends the specified data to the end of the sequence.       | `sb.append(" World");` // "Hello World"                      |
| `insert(int offset, ...)`                 | Inserts data at the specified position.                      | `sb.insert(6, "Java ");` // Inserts at index 6               |
| `replace(int start, int end, String str)` | Replaces the characters in a substring of this sequence with the specified string. | `sb.replace(11, 16, "Earth");` // Replaces text from index 11 to 16 |
| `delete(int start, int end)`              | Removes the characters in a substring of this sequence.      | `sb.delete(5, 6);` // Deletes characters from index 5 to 6   |
| `deleteCharAt(int index)`                 | Removes the character at the specified position.             | `sb.deleteCharAt(5);` // Deletes character at index 5        |
| `reverse()`                               | Reverses the characters in this sequence.                    | `sb.reverse();` // Reverses the sequence                     |
| `toString()`                              | Converts the sequence of characters to a string.             | `String str = sb.toString();` // Converts to string          |
| `length()`                                | Returns the length (character count) of this sequence.       | `int len = sb.length();` // Gets the length                  |
| `setLength(int newLength)`                | Sets the length of the character sequence.                   | `sb.setLength(10);` // Sets length to 10                     |
| `charAt(int index)`                       | Returns the character at the specified index.                | `char c = sb.charAt(5);` // Gets character at index 5        |
| `setCharAt(int index, char ch)`           | Sets the character at the specified index to `ch`.           | `sb.setCharAt(5, 'X');` // Sets character at index 5 to 'X'  |

This table covers the most commonly used methods of the `StringBuilder` class in Java. Remember that `StringBuilder` is used for creating and manipulating strings dynamically, which can be more efficient than using immutable strings (`String`) when dealing with numerous or complex string operations.



## Collections 

Here are some of the most commonly used collections and how to use them:

1. **ArrayList**:
   - Description: A resizable array implementation of the List interface.
   - Usage:
     - `List<String> list = new ArrayList<>();`
     - `list.add("Apple");`
     - `list.get(0); // Accessing elements`
     - `list.remove(i); // Removing elements, i is index`
   
2. **LinkedList**:
   - Description: Implements List and Deque interfaces; useful for efficient insertion and removal at both ends.
   - Usage:
     - `List<String> linkedList = new LinkedList<>();`
     - `linkedList.add("Banana");`
     - `linkedList.addFirst("Apple"); // Adding at the beginning`
     - `linkedList.getLast(); // Accessing the last element`
   
3. **HashSet**:
   - Description: Implements the Set interface; it's an unordered collection that doesn't allow duplicate values.
   - Usage:
     - `Set<Integer> set = new HashSet<>();`
     - `set.add(1);`
     - `set.contains(1); // Checking for a value`
     - `set.remove(1);`
   
4. **TreeSet**:
   
   - Description: Implements the SortedSet interface; stores elements in a sorted (ascending) manner.
   - Usage:
     - `Set<String> treeSet = new TreeSet<>();`
     - `treeSet.add("Orange");`
     - `treeSet.first(); // Accessing the first element`
     - `treeSet.last(); // Accessing the last element`
   
5. **HashMap**:
   - Description: Implements Map interface; stores key-value pairs and allows fast retrieval based on key.
   
   - Usage:
     - `Map<String, Integer> map = new HashMap<>();`
     
     - `map.put("Key", 1);`
     
     - `map.get("Key"); // Accessing values`
     
     - `map.remove("Key");`
     
     - `map.computeIfAbsent(k, key -> new HashSet<>()).add(i);`
     
       - This line of code checks if the key 'k' exists in the map; if not, it creates a new HashSet for that key, and then adds the value 'i' to that HashSet.
     
     - `map.put(k, map.getOrDefault(k, 1) + 1);`
   
6. **TreeMap**:
   - Description: Implements the SortedMap interface; stores key-value pairs in a sorted order of keys.
   - Usage:
     - `Map<String, Integer> treeMap = new TreeMap<>();`
     - `treeMap.put("Key", 1);`
     - `treeMap.firstKey(); // Accessing the smallest key`
     - `treeMap.lastKey(); // Accessing the largest key`
   
7. **Queue/Deque**:
   - Description: Queue typically orders elements in FIFO (first-in-first-out) manner. Deque (double-ended queue) allows insertion and removal at both ends.
   - Usage:
     - `Queue<String> queue = new LinkedList<>();`
     - `queue.offer("Hello"); // Adding elements`
     - `queue.poll(); // Removing elements`
     - `Deque<String> deque = new ArrayDeque<>();`
     - `deque.addFirst("First"); // Adding at the beginning`
     - `deque.addLast("Last"); // Adding at the end`
   
8. **PriorityQueue**:
   
   - Description: Heap is a tree-like data structure that satisfies the heap property: In a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C. In a min heap, the opposite is true. [Heap is often used to implement priority queues or sorting algorithms](https://otda.ny.gov/programs/heap/)[1](https://otda.ny.gov/programs/heap/).
   - Usage:
     - `PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // Create a min-heap`
     - `PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder()); // Create a max-heap`
     - `minHeap.add(10); // Add an element to the heap`
     - `maxHeap.remove(); // Remove the root element (the maximum or minimum) from the heap`
     - `minHeap.peek(); // Get the root element without removing it`



### How to use collections

Here's a table detailing how to best use common Java collections, highlighting their ideal usage scenarios, features, and key considerations:

| Collection      | Best Use Cases                                               | Key Features                                                 | Considerations                                               |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **ArrayList**   | Fast access to elements by index. Ideal for storing and accessing large amounts of data. | Dynamic resizing, but resizing can be slow. Fast random access. | Not efficient for frequent insertion or deletion at the middle or beginning. |
| **LinkedList**  | Frequent additions and removals from the beginning or middle. | Fast insertion and removal. Doubly-linked list.              | Slower random access. Iteration can be slower than ArrayList. |
| **HashSet**     | Operations requiring uniqueness of elements (no duplicates). Fast access and modification. | Uses hashing, offers constant-time performance for basic operations. | No order maintenance, element order may change.              |
| **TreeSet**     | Maintaining a sorted set according to natural ordering or custom Comparator. | Maintains sorted order, log(n) time cost for basic operations. | Slower operations compared to HashSet.                       |
| **HashMap**     | Storing key-value pairs for quick lookup by key.             | Constant-time performance for get and put, uses hashing.     | No ordering of entries, requires good hash functions.        |
| **TreeMap**     | Storing key-value pairs in sorted order, range operations on keys. | Sorted according to natural ordering or Comparator, log(n) performance for basic operations. | Slower than HashMap, but maintains order.                    |
| **Queue/Deque** | FIFO processing (Queue). LIFO and FIFO (Deque).              | Queue: FIFO order. Deque: Supports element insertion and removal at both ends. | Not suitable for random access of elements.                  |

This table should provide a clear overview of when and how to use each type of collection in Java, factoring in their strengths and limitations. It's a great addition to your cheat sheet for quick and effective reference.



### How to iterate

Iterating over collections in Java can be done in several ways, depending on the type of collection and your specific requirements. Here's a guide on how to iterate over the common collections:

1. **ArrayList and LinkedList (List Interface)**:
   - **For-each Loop**: Ideal for iterating when you don't need the index.
     ```java
     for(String element : list) {
         System.out.println(element);
     }
     ```
   - **Iterator**: Useful when you need to remove elements during iteration.
     ```java
     Iterator<String> iterator = list.iterator();
     while(iterator.hasNext()) {
         String element = iterator.next();
         // iterator.remove(); // If you need to remove the element
         System.out.println(element);
     }
     ```
   - **For Loop with Index**: When you need the index.
     ```java
     for(int i = 0; i < list.size(); i++) {
         System.out.println(list.get(i));
     }
     ```

2. **HashSet and TreeSet (Set Interface)**:
   - **For-each Loop**: Simplest way to iterate over a set.
     ```java
     for(Integer element : set) {
         System.out.println(element);
     }
     ```
   - **Iterator**: When removal of elements during iteration is required.
     ```java
     Iterator<Integer> iterator = set.iterator();
     while(iterator.hasNext()) {
         Integer element = iterator.next();
         System.out.println(element);
     }
     ```

3. **HashMap and TreeMap (Map Interface)**:
   - **For-each Loop on EntrySet**: Iterate over key-value pairs.
     ```java
     for(Map.Entry<String, Integer> entry : map.entrySet()) {
         System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
     }
     ```
   - **For-each Loop on KeySet or Values**: When you need only keys or values.
     ```java
     // For Keys
     for(String key : map.keySet()) {
         System.out.println("Key: " + key);
     }
     
     // For Values
     for(Integer value : map.values()) {
         System.out.println("Value: " + value);
     }
     ```
   - **Iterator on EntrySet**: For removing elements while iterating.
     ```java
     Iterator<Map.Entry<String, Integer>> iterator = map.entrySet().iterator();
     while(iterator.hasNext()) {
         Map.Entry<String, Integer> entry = iterator.next();
         System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
     }
     ```

4. **Queue/Deque**:
   - **For-each Loop**: Standard iteration, without considering the queue nature.
     ```java
     for(String element : queue) {
         System.out.println(element);
     }
     ```
   - **While Loop with Poll**: If you want to iterate and remove elements in FIFO order.
     ```java
     while(!queue.isEmpty()) {
         System.out.println(queue.poll());
     }
     ```

Each iteration method serves different purposes. The choice of which to use depends on whether you need to access the index, remove elements during iteration, or maintain the order (especially for sorted collections).



## Operators

Here are seven tables, each dedicated to a different category of common operators in Java:

1. **Arithmetic Operators**

   | Operator | Description         | Example | Result    |
   | -------- | ------------------- | ------- | --------- |
   | `+`      | Addition            | `5 + 3` | `8`       |
   | `-`      | Subtraction         | `5 - 3` | `2`       |
   | `*`      | Multiplication      | `5 * 3` | `15`      |
   | `/`      | Division            | `5 / 3` | `1` (int) |
   | `%`      | Modulus (Remainder) | `5 % 3` | `2`       |

2. **Relational Operators**

   | Operator | Description              | Example  | Result  |
   | -------- | ------------------------ | -------- | ------- |
   | `==`     | Equal to                 | `5 == 3` | `false` |
   | `!=`     | Not equal to             | `5 != 3` | `true`  |
   | `>`      | Greater than             | `5 > 3`  | `true`  |
   | `<`      | Less than                | `5 < 3`  | `false` |
   | `>=`     | Greater than or equal to | `5 >= 3` | `true`  |
   | `<=`     | Less than or equal to    | `5 <= 3` | `false` |

3. **Logical Operators**

   | Operator | Description | Example                | Result  |
   | -------- | ----------- | ---------------------- | ------- |
   | `&&`     | Logical AND | `(5 > 3) && (5 > 4)`   | `true`  |
   | `||`     | Logical OR  | `(5 > 3) \|\| (5 < 4)` | `true`  |
   | `!`      | Logical NOT | `!(5 > 3)`             | `false` |

4. **Assignment Operators**

   | Operator | Description         | Example  | Equivalent To |
   | -------- | ------------------- | -------- | ------------- |
   | `=`      | Assign              | `a = 5`  |               |
   | `+=`     | Add and assign      | `a += 3` | `a = a + 3`   |
   | `-=`     | Subtract and assign | `a -= 3` | `a = a - 3`   |
   | `*=`     | Multiply and assign | `a *= 3` | `a = a * 3`   |
   | `/=`     | Divide and assign   | `a /= 3` | `a = a / 3`   |
   | `%=`     | Modulus and assign  | `a %= 3` | `a = a % 3`   |

5. **Bitwise Operators**

   | Operator | Description          | Example   | Result (if `a = 5` and `b = 3`) |
   | -------- | -------------------- | --------- | ------------------------------- |
   | `&`      | Bitwise AND          | `a & b`   | `1`                             |
   | `|`      | Bitwise OR           | `a | b`   | `7`                             |
   | `^`      | Bitwise XOR          | `a ^ b`   | `6`                             |
   | `~`      | Bitwise Complement   | `~a`      | `-6`                            |
   | `<<`     | Left shift           | `a << 1`  | `10`                            |
   | `>>`     | Right shift          | `a >> 1`  | `2`                             |
   | `>>>`    | Unsigned right shift | `a >>> 1` | `2`                             |

6. **Unary Operators**

   | Operator | Description | Example        | Result (if `a = 5`) |
   | -------- | ----------- | -------------- | ------------------- |
   | `+`      | Unary plus  | `+a`           | `5`                 |
   | `-`      | Unary minus | `-a`           | `-5`                |
   | `++`     | Increment   | `a++` or `++a` | `6`                 |
   | `--`     | Decrement   | `a--` or `--a` | `4`                 |

7. **Ternary Operator**

   | Operator | Description                     | Example            | Result                 |
      |----------|----------------------------------|--------------------|------------------------|
      | `?:`     | Conditional (Ternary) Operator   | `(5 > 3) ? "Yes" : "No"` | `"Yes"`         |



## Collections Method Usage

Certainly! Here's the updated table with the `swap` method added:

| Method                                                       | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `sort(List<T> list)`                                         | Sorts the specified list into ascending order, according to the natural ordering of its elements. |
| `reverse(List<?> list)`                                      | Reverses the order of the elements in the specified list.    |
| `shuffle(List<?> list)`                                      | Randomly permutes the specified list using a default source of randomness. |
| `binarySearch(List<? extends Comparable<? super T>> list, T key)` | Searches the specified list for the specified object using the binary search algorithm. |
| `swap(List<?> list, int i, int j)`                           | Swaps the elements at the specified positions in the specified list. |
| `copy(List<? super T> dest, List<? extends T> src)`          | Copies all of the elements from one list into another.       |
| `fill(List<? super T> list, T obj)`                          | Replaces all of the elements of the specified list with the specified element. |
| `frequency(Collection<?> c, Object o)`                       | Returns the number of elements in the specified collection equal to the specified object. |
| `max(Collection<? extends T> coll)`                          | Returns the maximum element of the given collection, according to the natural ordering of its elements. |
| `min(Collection<? extends T> coll)`                          | Returns the minimum element of the given collection, according to the natural ordering of its elements. |
| `addAll(Collection<? super T> c, T... elements)`             | Adds all of the specified elements to the specified collection. |

The `swap` method, as mentioned earlier, is used to swap the elements at two specified positions in a list.



