class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right

def arrayToBST(arr:list):
    if not arr:
        return None
    arr=sorted(arr)
    mid=(len(arr))//2
    root=TreeNode(arr[mid])
    root.left=arrayToBST(arr[:mid])
    root.right=arrayToBST(arr[mid+1:])
    return root

def preorder(root:TreeNode):
    if not root:
        return
    print(root.val,end=" ")
    preorder(root.left)
    preorder(root.right)

if __name__=="__main__":
    print("Enter no.of test cases ",end=" ")
    for _ in range(int(input())):
        arr=list(map(int, input("Enter array elements: ").split()))
        root=arrayToBST(arr)
        preorder(root)