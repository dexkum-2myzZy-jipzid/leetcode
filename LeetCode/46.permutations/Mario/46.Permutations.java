class Solution {

    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {
        backtracking(new ArrayList<Integer>(), nums);
        return res;
    }

    private void backtracking(ArrayList<Integer> order, int[] left) {
        if (left.length == 0) {
            res.add(new ArrayList<>(order));
            return;
        }

        for (int i = 0; i < left.length; i++) {
            order.add(left[i]);
            int[] newLeft = new int[left.length - 1];
            for (int j = 0; j < newLeft.length; j++) {
                int leftIdx = j;
                if (j >= i) {
                    leftIdx += 1;
                }
                newLeft[j] = left[leftIdx];
            }
            backtracking(order, newLeft);
            order.remove(order.size() - 1);
        }
    }
}