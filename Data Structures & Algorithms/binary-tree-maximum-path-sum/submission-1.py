class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def helper(node):
            nonlocal res

            if not node:
                return 0

            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)

            # Best path whose highest point is this node
            res = max(
                res,
                node.val + left + right
            )

            # Return a path that parent can continue
            return node.val + max(left, right)

        helper(root)
        return res


        