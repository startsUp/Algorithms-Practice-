/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
  // Extra Space solution
  public Node copyRandomList(Node head) {
      if (head == null) return null;
      HashMap<Node,Integer> map = new HashMap();
      
      Node temp = head;
      int index = 0;
      while (temp != null){
          map.put(temp, index);
          index++;
          temp = temp.next;
      }
      
      Node[] arr = new Node[index+1];
      
      index = 0;
      Node copyHead = new Node(head.val);
      arr[index] = copyHead;
      temp = copyHead;
      while (head != null) {
          index++;
          if (head.next != null){
              if (arr[index] == null){
                  Node next = new Node(head.next.val);
                  temp.next = next;
                  arr[index] = next;
              } 
              else temp.next = arr[index];    
          }
       
          if (head.random != null){
              Integer randomIndex = map.get(head.random);
              Node random = arr[randomIndex];
              if (random == null){
                  random = new Node(head.random.val);
                  arr[randomIndex] = random;
              }
              temp.random = random;
          }
          temp = temp.next;
          head = head.next;
      }
      
      return copyHead;
  }

  // No extra Space solution
  public Node copyRandomList2(Node head) {
    Node iter = head, next;

    // First round: make copy of each node,
    // and link them together side-by-side in a single list.
    while (iter != null) {
      next = iter.next;
  
      Node copy = new Node(iter.label);
      iter.next = copy;
      copy.next = next;
  
      iter = next;
    }
  
    // Second round: assign random pointers for the copy nodes.
    iter = head;
    while (iter != null) {
      if (iter.random != null) {
        iter.next.random = iter.random.next;
      }
      iter = iter.next.next;
    }
  
    // Third round: restore the original list, and extract the copy list.
    iter = head;
    Node pseudoHead = new Node(0);
    Node copy, copyIter = pseudoHead;
  
    while (iter != null) {
      next = iter.next.next;
  
      // extract the copy
      copy = iter.next;
      copyIter.next = copy;
      copyIter = copy;
  
      // restore the original list
      iter.next = next;
  
      iter = next;
    }
  
    return pseudoHead.next;
  }
}