class Node:
    def __init__(self,data) -> None:
        self.val = data
        self.left = None
        self.right = None

def insertLevOrd(arr:list,root,i:int,n:int):
    if i<n:
        temp = Node(arr[i])
        root = temp
        root.left = insertLevOrd(arr,root.left,2*i+1,n)
        root.right = insertLevOrd(arr,root.right,2*i+2,n)
    return root

def findValue(node:Node,key):
    if node==None:
        return None
    if node.val == key:
        return node
    
    l = findValue(node.left,key)
    if l:
        return l
    r =findValue(node.right,key)
    if r:
        return r

if __name__=="__main__":
    print("No. of testcases : ")
    for _ in range(int(input())):
        print("Enter tree in level order: ")
        arr =list(map(int, input().split()))
        root=None
        root=insertLevOrd(arr,root,0,len(arr))
    print("Enter value to find in the tree: ")
    k=int(input())
    print(findValue(root,k))