class Node:
    def __init__(self,data) -> None:
        self.val = data
        self.left = None
        self.right = None

def insertLevOrd(arr:list,root,i:int,n:int)->Node:
    if i<n:
        temp = Node(arr[i])
        root = temp
        root.left = insertLevOrd(arr,root.left,2*i+1,n)
        root.right = insertLevOrd(arr,root.right,2*i+2,n)
    return root

def findLCA(root:Node, n1:int, n2:int)->Node:
    if not root:
        return None
    if root.val==n1 or root.val==n2:
        return root

    l_lca=findLCA(root.left,n1,n2)
    r_lca=findLCA(root.right,n1,n2)

    if l_lca and r_lca:
        return root
    
    return l_lca if l_lca is not None else r_lca

if __name__=="__main__":
    print("No. of testcases : ")
    for _ in range(int(input())):
        # print("Enter tree in level order: ")
        arr =list(map(int, input("Enter tree in level order: ").split()))
        root=None
        root=insertLevOrd(arr,root,0,len(arr))
        k=list(map(int, input("Enter nodes for which LCA to be found: ").split()))
        print(findLCA(root,k[0],k[1]).val) # the .val is not needed if problem needed reference of the object
        