class Solution(object):
    def FindTwoNodes(self, root):
        if root:
            self.FindTwoNodes(root.left)
            if self.pre and self.pre.val >= root.val:
                self.n2 = root
                if not self.n1:
                    self.n1 = self.pre
            self.pre = root.val
            self.FindTwoNodes(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.n1, self.n2 = None, None
        self.pre = None
        self.FindTwoNodes(root)