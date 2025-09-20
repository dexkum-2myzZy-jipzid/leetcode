class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int num : nums) {
            maxHeap.add(num);
        }

        for (int i = k; k > 1; k--) {
            maxHeap.remove();
        }

        return maxHeap.peek();
    }
}