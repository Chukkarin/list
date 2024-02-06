class BinarySearchTree:
    def __init__(self):
        self.data = []

    def add_node(self, key):
        self._add_node(0, key)

    def _add_node(self, index, key):
        if index >= len(self.data):
            self.data.extend([None] * (index - len(self.data) + 1))

        if self.data[index] is None:
            self.data[index] = key
        elif key < self.data[index]:
            self._add_node(2 * index + 1, key)
        else:
            self._add_node(2 * index + 2, key)

    def print_asc(self, index=0):
        if index < len(self.data) and self.data[index] is not None:
            self.print_asc(2 * index + 1)
            print(self.data[index], end=" ")
            self.print_asc(2 * index + 2)

    def print_desc(self, index=0):
        if index < len(self.data) and self.data[index] is not None:
            self.print_desc(2 * index + 2)
            print(self.data[index], end=" ")
            self.print_desc(2 * index + 1)


# Example usage:
binarySearchTree = BinarySearchTree()
binarySearchTree.add_node(5)
binarySearchTree.add_node(15)
binarySearchTree.add_node(2)
binarySearchTree.add_node(9)
binarySearchTree.add_node(20)
binarySearchTree.add_node(1)
binarySearchTree.add_node(4)
binarySearchTree.add_node(8)
binarySearchTree.add_node(9)
binarySearchTree.add_node(17)

print("Ascending Order:")
binarySearchTree.print_asc()
print("\nDescending Order:")
binarySearchTree.print_desc()