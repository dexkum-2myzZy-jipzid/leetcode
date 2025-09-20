/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    // iterate l1 and l2 simultaneously, get their vals
    // plus is 0 at first
    // val1 + val2 + plus, if > 9, the plus is 1 else 0
    
    dummy := &ListNode{1, nil}
    node := dummy
    plus := 0

    for l1 != nil || l2 != nil {
        val := plus
        if l1 != nil {
            val += l1.Val
            l1 = l1.Next
        }

        if l2 != nil {
            val += l2.Val
            l2 = l2.Next
        }

        if val > 9 {
            plus = 1
        }else{
            plus = 0
        }

        node.Next = &ListNode{val%10, nil}
        node = node.Next
    }

    if plus > 0 {
        node.Next = &ListNode{plus, nil}
    }

    return dummy.Next
}