class Node:
    def __init__(self,data) -> None:
        self.val = data
        self.next = None

class TreeNode:
    def __init__(self,data) -> None:
        self.val = data
        self.right = self.left = None

def insertLevOrd(arr:list,root,i:int,n:int):
    if i<n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insertLevOrd(arr,root.left,2*i+1,n)
        root.right = insertLevOrd(arr,root.right,2*i+2,n)
    return root

def sortedList(head:Node,root:TreeNode):
    if not root:
        return head

    head = sortedList(head,root.left)
    newNode = Node(root.val)
    temp=head
    prev = None
    
    if not temp:
        head = newNode
    else:
        while temp:
            if temp.val > root.val:
                break
            else:
                prev= temp
                temp=temp.next
        if not temp:
            prev.next = newNode
        else:
            if not prev:
                newNode.next = temp
                head = newNode
            else:
                newNode.next = temp
                prev.next = newNode
    head=sortedList(head,root.right)
    return head

def printL(head:Node):
    if not head:
        return
    temp = head
    while temp:
        print(temp.val,end= " ")
        temp=temp.next

def main():
    print("No. of testcases : ")
    
    for _ in range(int(input())):
        print("Enter tree in level order: ")
        arr =list(map(int, input().split()))
        root=None
        root=insertLevOrd(arr,root,0,len(arr))
        head = sortedList(None, root)
        print("\nSorted List: ")
        printL(head)
    

if __name__=="__main__":
    main()