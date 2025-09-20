func containsDuplicate(nums []int) bool {
    m := make(map[int]bool, len(nums))
    for _, num := range nums {
        if _, exist := m[num]; exist {
            return true
        }else{
            m[num] = true
        }
    }
    return false
}