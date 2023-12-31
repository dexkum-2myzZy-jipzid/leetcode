class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0){
            return null;
        }
        ListNode dummy = new ListNode(-1);
        ListNode p = dummy;

        PriorityQueue<ListNode> pq = new PriorityQueue<>((a,b) -> (a.val - b.val));

        for(ListNode head : lists){
            if(head != null){
                pq.offer(head);
            }
        }

        while(!pq.isEmpty()){
            ListNode node = pq.poll();
            p.next = node;
            if(node.next != null){
                pq.offer(node.next);
            }
            p = p.next;
        }

        return dummy.next;
    }
}