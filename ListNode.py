

class GlobalWealth(object):
    def __init__(self):
        self._global_wealth = 10.0
        self._observers = []

    @property
    def global_wealth(self):
        return self._global_wealth

    @global_wealth.setter
    def global_wealth(self, value):
        self._global_wealth = value
        for callback in self._observers:
            print('announcing change')
            callback(self._global_wealth)

    def bind_to(self, callback):
        print('bound')
        self._observers.append(callback)


class Person(object):
    def __init__(self, data):
        self.wealth = 1.0
        self.data = data
        self.data.bind_to(self.update_how_happy)
        self.happiness = self.wealth / self.data.global_wealth

    def update_how_happy(self, global_wealth):
        self.happiness = self.wealth / global_wealth




# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

#     def __repr__(self) -> str:
#         return f"ListNode{{val: {self.val} , next: {self.next}}}"
        

# def createLinkedList(data = []):
#     # i = 0
#     # while i < len(data):
#     val = data.pop(0)
#     if len(data) == 0:
#         return ListNode(val)    
#     else:
#         return ListNode(val,createLinkedList(data))
# def dosomething(x):
#     x = x + 1
#     return x
# if __name__ == "__main__":
#     x = 1
#     dosomething(x)
#     print(x, dosomething(x))
    

    # array = [1,2,3,4,5,6,7,8,9]
    # middle = len(array) // 2
    # print(array)
    
    # head = createLinkedList(array)
    # p1 = p2 = head
    
    # print(middle, len(array))
    # for i in range(0,middle - 1):
    #     p2 = p2.next
    #     print(i, p2, head)

    # p2.next = p2.next.next
    # print(head)
