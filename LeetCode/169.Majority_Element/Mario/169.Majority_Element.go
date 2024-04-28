func majorityElement(nums []int) int {
    var res, count int

    for _, num := range nums {
        if(count == 0){
            res = num;
        }
        if num == res{
            count += 1
        }else{
            count -= 1
        }
    }

    return res
}