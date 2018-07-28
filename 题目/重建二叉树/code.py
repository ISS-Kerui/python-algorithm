class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre)==0:
            return None
        root_data = TreeNode(pre[0])#将根定义成节点的形式
        i=tin.index(pre[0])#i=tin.index(root_data.val)#寻找位置将左右子树分开
        root_data.left = self.reConstructBinaryTree(pre[1:1+i],tin[:i])
        root_data.right = self.reConstructBinaryTree(pre[1+i:],tin[i+1:])
        return root_data