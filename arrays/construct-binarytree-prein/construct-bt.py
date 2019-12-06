class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        indices = {}
        for i in range(len(inorder)):
            indices[inorder[i]] = i
        
        head = TreeNode(preorder[0])
        stack = [[head, -1, len(inorder), 0]]
        while stack:
           
            cur = stack[-1]
            head = cur[0]

            # build left tree, if cur index is within bounds
            if indices[cur[0].val] - 1 > cur[1]:
                node = TreeNode(preorder[cur[3]+1])
                head.left = node
                stack.append([node, cur[1], indices[cur[0].val], cur[3]+1])
                cur[1] = indices[cur[0].val]
                continue
            if indices[cur[0].val] + 1 < cur[2]:
                node = TreeNode(preorder[cur[3]+1])
                head.right = node
                stack.append([node, indices[cur[0].val], cur[2], cur[3]+1])
                cur[2] = indices[cur[0].val]
                continue
            ind = stack[-1][3]
            stack.pop()
            if stack:
                stack[-1][3] = ind
            
        return head