var diameter int
func diameterOfBinaryTree(root *TreeNode) int {
    diameter = 0
    longestPath(root)
    return diameter
}

func longestPath(node *TreeNode) int{
    if node == nil {
        return 0
    }

    left := longestPath(node.Left)
    right := longestPath(node.Right)

    diameter = max(diameter, left + right)

    return max(left, right) + 1
}