class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return "ListNode{val: " + str(self.val) + ", next: " + str(self.next) + "}"
        

def createLinkedList(data = []):
    # i = 0
    # while i < len(data):
    val = data.pop(0)
    if len(data) == 0:
        return ListNode(val)    
    else:
        return ListNode(val,createLinkedList(data))

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8,9]
    middle = len(array) // 2
    print(array)
    
    head = createLinkedList(array)
    p1 = p2 = head
    
    print(middle, len(array))
    for i in range(0,middle - 1):
        p2 = p2.next
        print(i, p2, head)

    p2.next = p2.next.next
    print(head)
    # for i in range(len(array)):
    #     if i < len(array)-1:
    #         head = ListNode(array[i], ListNode([i+1]))
    #     else:
    #         head = ListNode(array[i])
    # print(head)
