from binary_search_tree import Tree, TreeNode

def height(node):
    if node == None:
        return -1

    return node.height

class AVLTree(Tree):
    def insert(self, node):
        super(self.__class__, self).insert(node)
        self.balance(node)

    def delete(self, node):
        new = super(self.__class__, self).delete(node)
        self.balance(new);

    def balance(self, node):
        while node != None:
            self._update_height(node)
            left = node.leftChild
            right = node.rightChild

            if height(left) > height(right) + 1: # left heavy
                if left.leftChild != None: # all left
                    self._right_rotate(node)
                elif left.rightChild != None: # left, right, left
                    self._left_rotate(left)
                    self._right_rotate(node)
            elif height(right) > height(left) + 1: # right heavy
                if right.rightChild != None: # all right
                    self._left_rotate(node)
                elif right.leftChild != None: # right, left, right
                    self._right_rotate(right)
                    self._left_rotate(node)

            node = node.parent

    def _right_rotate(self, a):
        b = a.leftChild
        b.parent = a.parent

        if b.parent == None:
            self.root = b
        else:
            if a.parent.leftChild == a:
                a.parent.leftChild = b
            elif a.parent.rightChild == a:
                a.parent.rightChild = b

        a.leftChild = b.rightChild

        if a.leftChild != None:
            a.leftChild.parent = a

        b.rightChild = a
        a.parent = b
        self._update_height(a)
        self._update_height(b)

    def _left_rotate(self, a):
        b = a.rightChild
        b.parent = a.parent

        if b.parent == None:
            self.root = b
        else:
            if a.parent.leftChild == a:
                a.parent.leftChild = b
            elif a.parent.rightChild == a:
                a.parent.rightChild = b

        a.rightChild = b.leftChild

        if a.rightChild != None:
            a.rightChild.parent = a

        b.leftChild = a
        a.parent = b
        self._update_height(a)
        self._update_height(b)

    def _update_height(self, node):
        node.height = max(height(node.leftChild), height(node.rightChild)) + 1
