"# LeetCode" 

public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {

        int sum = 0;
        ListNode result = new ListNode(0);
        ListNode current = result;

        while (l1 != null || l2 != null || sum > 0){
            if (l1 != null){
                sum += l1.val;
                l1 = l1.next;
            }

            if (l2 != null){
                sum += l2.val;
                l2 = l2.next;
            }

            current.next = new ListNode(sum % 10);
            sum = sum/10;
            current = current.next;
        }

        return result.next;
    }
}