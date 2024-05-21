func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i, num := range(nums) {
		index, ok := m[num]
		if ok {
			return []int{index, i}
		} else {
			m[target-num] = i
		}
	}
	return []int{0,0}
}