# Node Structure
## Within the construc of the C Structure this holds many similarities
    THe Node is more or less the heart of the C Implementation of many Data Structures. The node points to the next element that is wanted from within the applied data structure. Attempts to get this as close to Pointer Arithmetic as possible, without fully corrupting the Python Value in itself.
    As the Node Structure changes new variables need to be added to it, and move along with whatever may be needed.
### Implementations of Node Struct

  
##### Implementation for the Linked List Data Structure
```python
'''
Implementation of the Node Data Class. 
It is not so much a class implementation as it is a structure.
'''

class Node(object):
    __totalNodes = 0
    """docstring for Node
    Implementation of the Node Structure.
    Used to simulate the Node Structs within C, and other languages that 
    allow for pointer arithmetic.
    Base Functionality: An ability to get to the next Node from the current one
        addNode(): Append a node to the input (List)
        setNode(): Sets the value of the left, or right node of current node being pointed to.
        getContent(): Get __contents__ of the current Node Pointed To.

    """
    def __init__(self, contents=None,leftNode=None, rightNode=None):
        super(Node, self).__init__()
        self.__leftNode = leftNode
        self.__rightNode= rightNode
        self.__contents = contents
        self.__index = 0
        # Datatype of the content contained in the node.
        self.__setDataType(contents)
        # Increment the count of the nodes that have been created.
        self.__totalNodes+=1
        
    # Destructor Function. Can do a bit of error Logging, but don't need to atm.
    def __del__(self):
        self.__totalNodes-=1

    # OverLoad the str function. Prints the address of the Node, and it's contents.
    def __str__(self):  
        addr=repr(self).split(' ')[-1][:-1]
        return str('Addr: {0}\tContents: {1}'.format(addr, self.__contents))
    
    '''
    Add a node to the list being dealt with. 
    If adding a node to the left, make the newNode that is 
    created point to the previous node. Ie.
    if adding a node to the left of the list, then 
    then the new nodes rightNode has to be the left Node
    of the node that called it, and vice versa.
    '''
    def addNode(self, prevNode, nextDir, contents=None):
        prevDir = 'right' if nextDir == 'left' else 'left'
        
        # Create a new node
        nextNode=Node(contents)
        
        # Make the new node point to the one that called it, based on direction
        nextNode.setNode(prevDir, prevNode)
        
        # Index is incremented if adding to the right of the list, else decrement
        nextInd=prevNode.get_index()+(-1 if nextDir == 'left' else 1)
        nextNode.setIndex(nextInd )

        # Make the node that called add acknowledge that the node 
        # that is created is to be pointed to next.
        prevNode.set_node(nextDir, nextNode)

    '''
    Getter Functions for the Node Class
    Return the needed element contained in the node, and do so without mutating anything
    '''
    # Gets the next node, to the left or right based on direction0|1
    # Useful for traversal of the given list that is brought in.
    def getNode(self, direction):
        if direction == 'left':
            return self.__leftNode
        elif direction == 'right':
            return self.__rightNode
        elif direction == 'this':
            return self 

    # Returns the content of current node. 
    def getContent(self):
        return self.__contents

    # Return the index of the value that is being referenced.
    def getIndex(self):
        return self.__index

    def getDataType(self):
        return self.__dataType

    '''
    Setter functions for the Node Class.
    Mutate the value that is needed, obscuring the class as much as possible.
    '''
    def setIndex(self, ind):
        self.__index=ind

    def setContent(self, contents):
        # Changing content, might change the data type.
        self.__setDataType(contents)
        self.__contents = contents

    # Simulation of the freeing up the node. Destructor, past __del__
    def setNode(self, direction, node=None):
        # Free's up either the left or right node, if no new node is passed in
        # Else makes the left|right point to the node passed in.
        if direction == 'left':
            self.__leftNode = node
        elif direction == 'right':
            self.__rightNode= node
        # The setter function will not work properly if referenced.
        # Have to create the wrapper on the actual Node created.
        elif direction == 'this':
            if node == None:
                self.__del__()
        else:
            print('Not given a handle to operate on.')
            return 1

    # User should absouletly never call this function. Done on creation of new
    # Nodes. Will attempt to grant type safety if appending a node to an existing
    # Data Structure. 
    def __setDataType(self, newContent):
        self.__dataType=type(newContent)
```