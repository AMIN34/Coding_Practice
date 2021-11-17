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

def identicalTrees(a:TreeNode,b:TreeNode)->bool:
    if a is None and b is None:
        return True
    if a is not None and b is not None:
        return ((a.val==b.val) and identicalTrees(a.left,b.left) and identicalTrees(a.right,b.right))
    return False

def main():
    print("Enter no.of test cases: ")
    for _ in range(int(input())):
        print("Enter 1st tree in level order: ")
        arr =list(map(int, input().split()))
        a=None
        a=insertLevOrd(arr,a,0,len(arr))
        arr =list(map(int, input().split()))
        b=None
        b=insertLevOrd(arr,b,0,len(arr))
        print(identicalTrees(a,b))

if __name__=="__main__":
    main()