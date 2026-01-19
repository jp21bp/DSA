###### Data structures
    # This file will contain varying data structures in python

##### Importing libraries
import ctypes
from typing import Any, Generator, Optional

##### C-style array
class CArray:
    def __init__(self, size: int) -> None:
        if size < 0: 
            raise ValueError("Size needs to be positive")
        self._size = size
        self._data = (ctypes.py_object * self._size)()
        self._type: Optional[type] = None
        self.clear()

    def clear(self, value: Optional[Any] = None) -> None:
        if self._type is not None and \
        value is not None and\
        not isinstance(value, self._type):
            raise TypeError(f"{self._type} not  {type(value)}")
        for i in range(self._size):
            self._data[i] = value
    
    def __len__(self) -> int:
        return self._size
    
    def __contains__(self, value: Any) -> bool:
        for item in self._data:
            if item == value:
                return True
        return False
    
    def _check_index(self, index: int) -> None:
        if not 0 <= index < self._size:
            raise IndexError("Index out of range")
        
    def __getitem__(self, index: int) -> Any:
        self._check_index(index)
        return self._data[index]
    
    def __setitem__(self, index: int, value: Any) -> None:
        if self._type is None and\
        value is not None:
            self._type = type(value)
        elif value is not None and not isinstance(value, self._type):
            raise TypeError(f"{self._type} not {type(value)}")
        self._check_index(index)
        self._data[index] = value

    def __iter__(self) -> Generator[Any, None, None]:
        yield from self._data

    def __reversed__(self) -> Generator[Any, None, None]:
        yield from reversed(self._data)

    def __str__(self) -> str: # print(x)
        return f"{self.__class__.__name__} [{', '.join(map(str,self._data))}]"
    
    def __repr__(self) -> str:  # print(repr(x))
        return f"{self.__class__.__name__} (size = {self._size})"


##### Experimenting with CArray
# arr = CArray(5)
# print(arr)





















##### Linked Lists 
#### Creating Node class
class Node:
    def __init__(self, data):
        self.data: int = data
        self.next: Node = None

    def __str__(self):
        return f"({self.data}) -> {self.next}"

### Experimenting with Node class
# node = Node(5)
# print(node)
    
#### Creating Linked List class
class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None

    def __str__(self) -> str:
        current = self.head
        result = ""
        result += "Head -> "
        while current:
            result += f"({current.data}) -> "
            current = current.next
        result += "None"
        return result
    
    def prepend(self, data) -> None:
        ## Add new node to beginning
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        ## Add new node to end of list
        new_node = Node(data)
        if not self.head:   #LList is empty
            self.head = new_node
            return
        last = self.head    #Start traversing from head
        while last.next:
            last = last.next    #Traverse all nodes
        last.next = new_node    #Add new node to tail, once tail is reached

    def delete_first(self, value) -> None:
        ## Eliminate the first node with "value"
        current: Node = self.head     #Where to start traversal
        prev: Node = None     # Keep track of prev node
            # Needed in order to connect linked list once target node is cut
        if current and current.data == value:  # Base case on first node
            # Only executes if both following scenarios are true:
                # Current != None => LList is NOT empty
                # Current.data == value => value is in the first node
            # Note, technically this base case is taken care of in the following while loop
                # BUT since it's the first node, it's easy to remove and maintain LList
                    # Specifically, there is no previous node to keep track of
                # Due to easiness, it's given it's own edge case
            self.head = current.next
            return
        while current and current.data != value:    #Value hasn't been found yet
            # There are 2 conditions that will BREAK from this while loop:
                # current == None => Either LList is empty or the tail has been reached
                # current.data == value => value has been found, so no need to keep traversing
            prev = current
            current = current.next
        if not current: #Either LList is empty or tail is reached
            print(f"Value {value} is not in linked list")
            return
        prev.next = current.next
        del current # Memory mgmt

    def delete_all(self, value) -> None:
        ## Deletes all nodes with "value"
            # Requires traversing ALL nodes 
        current = self.head     # Start of traversal
        prev = None     # Keep track of prev node 
            # Used to maintain linkness of list
        while self.head and self.head.data == value:
            # Base case: head node has value
            # while loop breaks only once head does NOT have "Value"
                # This ensures that many beginner nodes with "value" is checked
            self.head = current = self.head.next
        while current:  # Traverses all nodes
            # This while loop breaks on either conditions below:
                # LList is empty
                # Traversal has reached the tail
            if current.data == value: prev.next = current.next
                # Skip the current node
                # BUT still keep "prev" node as is
                    # In case there are multiple back-to-back nodes with "value"
            else: prev = current
                # Move the prev node the current node and continuje iteration
            current = current.next
                # Ensures the list will keep on traversing
            
        





### Experimenting with Linked List
llist = LinkedList()
llist.delete_first(5)
llist.append(1)
llist.append(2)
llist.prepend(3)
llist.delete_first(1)
llist.delete_first(3)
llist.append(3)
llist.append(3)
llist.append(1)
llist.prepend(3)
llist.prepend(3)
llist.delete_all(3)
llist.delete_first(1)
llist.delete_first(2)
print(llist)



























