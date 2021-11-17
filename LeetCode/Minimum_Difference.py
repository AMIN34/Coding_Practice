class TreeNode:
    def __init__(self,data) -> None:
        self.val=data
        self.left=self.right=None

def insertLevOrd(arr:list,root,i:int,n:int):
    if i<n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insertLevOrd(arr,root.left,2*i+1,n)
        root.right = insertLevOrd(arr,root.right,2*i+2,n)
    return root

def minDiff(a:TreeNode):
    return