/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

    public ListNode remover(ListNode head , int n){

        if(n==1){
            return head.next;
        }

        if(head.next == null){
            return null;
        }


        ListNode temp = head;

        int i = 1 ;

        // Navigate to the node before the target
        while(i<n-1){
            temp = temp.next;
            i++;
        }

        if(temp==null || temp.next==null){
            temp.next = null;
            return head;
        }

        // Remove the target node
        temp.next = temp.next.next;
        return head;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        int len = 0;
        ListNode temp = head;

        // First pass: calculate the length of the list
        while(temp!=null){
            temp = temp.next;
            len++;
        }

        // Convert nth from end to position from start
        int k = len - n +1;

        return remover(head , k);
    }
}