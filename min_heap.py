# Course: CS261 - Data Structures
# Assignment: 5
# Student: Srikanth Medicherla
# Description: This is Part 2: Min Heap Implementation. The methods here are add, get_min, remove_min, and build_heap.
# All of these methods help build and remove items from the heap to maintain the minimum heap properties. Special
# notice to build_heap which is constructed using O(n) complexity.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        This method adds a object to the MinHeap maintaining heap property. The runtime complexity of this
        implementation will be O(logN)
        """

        # First the node is added to the end of the array.
        self.heap.append(node)
        # current_index is our newest node and its index can be found by the self.heap's length - 1:
        current_index = self.heap.length() - 1
        # Given formula to find parent_index. // because we want the floor divisor, not the float divisor:
        parent_index = (current_index - 1) // 2
        # To maintain heap property, the child node must be less than or equal to the parent node
        while self.heap[current_index] < self.heap[parent_index] and parent_index >= 0:
            self.heap.swap(current_index,parent_index)
            current_index = parent_index
            parent_index = (current_index - 1) // 2

    def get_min(self) -> object:
        """
        This method returns an object with a minimum key without removing it from the heap. If the heap is empty,
        the method raises a MinHeapException. Runtime complexity will be in O(1)
        """

        if self.is_empty():
            raise MinHeapException
        return self.heap[0]

    def remove_min(self) -> object:
        """
        This method returns an object with a minimum key and removes it from the heap. If the heap is empty, the
        method raises a MinHeapException. The runtime complexity will be O(logN)
        """

        if self.is_empty():
            raise MinHeapException

        # We save the self.heap root:
        saved_node = self.get_min()

        # swap the root node with newest added node:
        self.heap.swap(0, self.heap.length()-1)

        # We pop the last element:
        self.heap.pop()

        # After popping and there are just 2 nodes, then simply swap them to maintain minHeap property.
        if self.heap.length() == 2:
            if self.heap[0] > self.heap[1]:
                self.heap.swap(0, 1)

        # Transport node down so heap follows the minHeap properties:
        current_index = 0
        while current_index * 2 + 1 < self.heap.length():
            # print("track these:", current_index * 2 + 2, self.heap.length())
            compare_index = current_index * 2 + 1
            if current_index * 2 + 2 < self.heap.length():
                if self.heap[current_index * 2 + 2] < self.heap[current_index * 2 + 1]:
                    compare_index = current_index * 2 + 2

            if self.heap[current_index] > self.heap[compare_index]:
                self.heap.swap(current_index, compare_index)
                current_index = compare_index
            else:
                current_index = self.heap.length()
        return saved_node

    def build_heap(self, da: DynamicArray) -> None:
        """
        This method receives a dynamic array with objects in any order and then builds a proper MinHeap form them.
        Current content of the MinHeap is lost. This method will build a heap with complexity of O(n)  time.
        """
        # step 1: clear the current content:
        while self.heap.length() > 0:
            self.heap.pop()

        # step 2: find parent of first non-leaf aka first node that isn't a (solo)minHeap. Doing this n/2 outer loop
        # combined with the percolating inner while loop creates an overall O(n) complexitiy.
        parent = ((da.length())//2) - 1

        # step 3: Percolate down with parent this subtree is a minHeap:
        # print(da[parent], da[parent * 2 + 2], da[parent * 2 + 1])
        while parent >= 0:
            while parent * 2 + 1 < da.length():
                minimum_kid = parent * 2 + 1
                if parent * 2 + 2 < da.length():
                    if da[parent * 2 + 2] < da[parent * 2 + 1]:
                        minimum_kid = parent * 2 + 2
                if da[parent] > da[minimum_kid]:
                    da.swap(parent, minimum_kid)
                    parent = minimum_kid
                else:
                    break
            # This indicates that it is O(n)?
            parent = parent - 1
        for node in da:
            self.heap.append(node)
        return


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)

