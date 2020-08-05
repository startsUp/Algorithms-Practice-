class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        traversed = []
        while stack:
            head = stack[-1]
            if(head.left):
                stack.append(head.left)
                head.left = None
                continue
            head = stack.pop()
            traversed.append(head.val)
            if(head.right):
                stack.append(head.right)
                head.right = None
                continue
        return traversed

    def inOrder(root): 
      
    # Set current to root of binary tree 
    current = root  
    stack = [] # initialize stack 
    done = 0 
      
    while True: 
          
        # Reach the left most Node of the current Node 
        if current is not None: 
              
            # Place pointer to a tree node on the stack  
            # before traversing the node's left subtree 
            stack.append(current) 
          
            current = current.left  
  
          
        # BackTrack from the empty subtree and visit the Node 
        # at the top of the stack; however, if the stack is  
        # empty you are done 
        elif(stack): 
            current = stack.pop() 
            print(current.data, end=" ") # Python 3 printing 
          
            # We have visited the node and its left  
            # subtree. Now, it's right subtree's turn 
            current = current.right  
  
        else: 
            break