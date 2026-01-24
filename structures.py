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
# llist = LinkedList()
# llist.delete_first(5)
# llist.append(1)
# llist.append(2)
# llist.prepend(3)
# llist.delete_first(1)
# llist.delete_first(3)
# llist.append(3)
# llist.append(3)
# llist.append(1)
# llist.prepend(3)
# llist.prepend(3)
# llist.delete_all(3)
# llist.delete_first(1)
# llist.delete_first(2)
# print(llist)


























##### Doubly linked lists
#### Create double nodes
class DoubleNode:
    def __init__(self, data) -> None:
        self.data: int = data
        self.next: DoubleNode = None
        self.prev: DoubleNode = None

    def __str__(self) -> str:
        next = f"({self.next.data})" if self.next else "None"
        prev = f"({self.prev.data})" if self.prev else "None"
        return f"{prev} <- ({self.data}) -> {next}"
        

### Trying out DoubleNode
# dnode = DoubleNode(5)
# print(dnode)



#### Creating Double Linked List
class DoubleLinkedList:
    def __init__(self) -> None:
        self.head: DoubleNode = None
        self.tail: DoubleNode = None

    def __str__(self) -> str:
        result = "Head -> "
        current = self.head
        if not current:
            result += "None <- Tail"
            return result
        while current:
            result += f"({current.data}) "
            current = current.next
            if current: result += "<-> " 
        result += "<- Tail"
        return result
    
    def print_nodes(self) -> str:
        # Iterates through all nodes and prints each node
            # Ensures that links are correct
        current = self.head
        i = 0
        result = ""
        if not current:
            return "No nodes exist"
        while current:  #Current is DoubleNode
            result += f"Node {i}: "
            result += str(current)
            result += '\n'
            current = current.next
            i += 1
        return result

    def prepend(self, data) -> None:
        ## Add new DoubleNode at beginning of list
        new_node = DoubleNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def append(self, data) -> None:
        ## Add new DOubleNode at end of list
        new_node = DoubleNode(data)
        if not self.tail:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_first(self, value) -> None:
        ## Delete first instance of "value"
        current = self.head
        if current and current.data == value:
            current.next.prev = None
            self.head = current.next
            return
        while current and current.data != value:    #Traverse
            current = current.next
        if not current:
            # Reaches end of traversal
                #I.e., all nodes have been checked and dismissed
            print(f"Value {value} not found in list")
            return
        current.prev.next = current.next
        if current.next: current.next.prev = current.prev
            # Node eliminated is in middle of list
        else: self.tail = current.prev
            # Node eliminated is one the LAST node of traversal
                # We need to change the head of linked list
                # Traversal wasn't quite complete
            # We already have case for when traversal was complete
                # I.e., for when all node have been checked and dismissed

    def delete_last(self, value) -> None:
        ## Deletes the last instance of "value"
        current = self.tail
        if current and current.data == value:
            current.prev.next = None
            self.tail = current.prev
            return
        while current and current.data != value:     #Traverse
            current = current.prev
        if not current:
            # Reaches end of traversal
                #I.e., all nodes have been checked and dismissed
            print(f"Value {value} not found in list")
            return
        current.next.prev = current.prev
        if current.prev: current.prev.next = current.next
            # Node eliminated is in middle of list
        else: self.head = current.next
            # Node eliminated is one the LAST node of traversal
                # We need to change the head of linked list
                # Traversal wasn't quite complete
            # We already have case for when traversal was complete
                # I.e., for when all node have been checked and dismissed

    def delete_all(self, value) -> None:
        ## Deletes all nodes with "Value"
        ## Will be done with forward traversal
            # But can also be done with backward traversal
        if not self.head: return    #Empty lsit
        while self.head.data == value:
            # Handles the case of head node being target
            self.head.next.prev = None
            self.head = self.head.next
        current = self.head.next
            # Since we already ensured that head node isn't target
        while current:
            # Only breaks AFTER the tail node has been checked
            if current.data == value:
                current.prev.next = current.next
                if current.next: current.next.prev = current.prev
                    #Eliminated node is in middle of list
                else: self.tail = current.prev
                    # Eliminated node is the LAST node in traversal
            current = current.next
        

#### Experimenting with Double Linked List
# dll = DoubleLinkedList()
# dll.prepend(5)
# dll.append(6)
# dll.prepend(3)
# dll.append(8)
# dll.append(6)
# dll.append(1)
# dll.prepend(2)
# dll.append(7)
# print(dll)
# dll.delete_first(3)
# print(dll)
# dll.delete_first(7)
# print(dll)
# dll.delete_last(5)
# print(dll)
# dll.delete_last(2)
# print(dll)
# dll.delete_all(1)
# print(dll)
# dll.delete_all(6)
# print(dll)
# # print(dll.print_nodes())
# print(f"Head node: {dll.head}")
# print(f"Tail node: {dll.tail}")
































##### Queues
    # Queues are like regular lines at the groceries
    # In order to ensure faireness (not being skipped), you
            # only need to keep track of the person in front of you
    # Thus this implies a single linked list
        # Linked: bc the order of arrival matters
        # Single: you don't need to keep track of the person behind you
            # But we can make it double to speed up operations
                # Tradeoff: memory and speed
    # However, if there is a dispute, you will need to keep track 
            # of the first and last peron on the line
        # The first person verifies they're next in line
        # The last person can verify the second to last person, etc
    # It also helps if you keep track of the size of the line
        # To allocate more resources, if necessary
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size = 0

    def enqueue(self, item):
        # Adds items to the end of the queue
        new_node = Node(item)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.next = self.tail
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        # Take care of the first node in line
        if not self.head: return None 
            #Line if empty
        data = self.head.data
        if self.head == self.tail:
            # THere is only ONE node in list
            self.head = self.tail = None
            return data
        current = self.tail
        prev = None
        while current != self.head:
            # Iterate to see who's next in line
            prev = current
            current = current.next
        self.head = prev
        self.size -= 1
        return data





































##### Creating Stack DS
class Stack:
    def __init__(self): self.items = []
    def is_empty(self): return self.items == []
    def push(self, item): self.items.append(item)
    def pop(self): return "empty" if self.is_empty() else self.items.pop()
    def peek(self): return "empty" if self.is_empty() else self.items[-1]
    def size(self): return len(self.items)























##### Hash tables
class HashTable:
    def __init__(self, size: int = 10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def __str__(self):
        items = []
        for i, bucket in enumerate(self.table):
            if bucket: items.append(f"Bucket {i}: {bucket}")
        return "\n".join(items)
    
    def _hash(self, key) -> int:
        # Hash function
        return hash(key) % self.size
            # "hash()" = built-in hash fcn

    def insert(self, key, value):
        # insert/update key-value pair
        index = self._hash(key)
        bucket = self.table[index]
        for i, (record_key, record_value) in enumerate(bucket):
            # This for-loop only runs is "bucket" is NOT EMPTY
            if record_key == key:
                # CHecks for COLLISION case
                bucket[i] = (key, value)    # UPDATE key,value pair
                return
        bucket.append((key, value))

    def get(self, key):
        # REtrieve value by key
        index = self._hash(key)
        bucket = self.table[index]
        for record_key, record_value in bucket:
            if record_key == key: return record_value
        raise KeyError("key not found")
    
    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (record_key, record_value) in enumerate(bucket):
            if record_key == key: 
                bucket.pop(i)
                return
        raise KeyError("key not found")
















