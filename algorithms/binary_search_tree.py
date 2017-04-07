class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, node):
        cur = self.root
        prev = None

        while cur != None:
            prev = cur

            if node.key < cur.key:
                cur = cur.leftChild
            else:
                cur = cur.rightChild

        node.parent = prev

        if prev == None:
            self.root = node
        elif prev.key > node.key:
            prev.leftChild = node
        else:
            prev.rightChild = node

    def delete(self, node):
        new_parent = None

        if node.leftChild == None:
            self._transplant(node, node.rightChild)
        elif node.rightChild == None:
            self._transplant(node, node.leftChild)
        else:
            new_parent = self.minimum(node.rightChild)

            if new_parent.parent != node:
                self._transplant(new_parent, new_parent.rightChild)
                new_parent.rightChild = node.rightChild
                new_parent.rightChild.parent = new_parent

            self._transplant(node, new_parent)
            new_parent.leftChild = node.leftChild
            new_parent.leftChild.parent = new_parent

        return new_parent

    def _transplant(self, parent, child):
        if parent.parent == None:
            self.root = child
        elif parent == parent.parent.leftChild:
            parent.parent.leftChild = child
        else:
            parent.parent.rightChild = child

        if child != None:
            child.parent = parent.parent

    def search(self, key):
        return self._search(key, self.root)

    def _search(self, key, start):
        if start == None or key == start.key:
            return start

        if start.key > key:
            return self._search(key, start.leftChild)
        else:
            return self._search(key, start.rightChild)

    def minimum(self, root=None):
        min = None

        if root == None:
            min = self.root
        else:
            min = root

        while min.leftChild != None:
            min = min.leftChild

        return min

    def maximum(self, root=None):
        max = None

        if root == None:
            max = self.root
        else:
            max = root

        while max.rightChild != None:
            max = max.rightChild

        return max

    def successor(self, node):
        if node.rightChild != None:
            return self.minimum(node.rightChild)

        p = node.parent

        while p != None and node == p.rightChild:
            p = p.parent

        return p

    def predecessor(self, node):
        if node.rightChild != None:
            return self.minimum(node.leftChild)

        p = node.parent

        while p != None and node == p.leftChild:
            p = p.parent

        return p

    def walk(self):
        self._in_order_walk(self.root)

    def _in_order_walk(self, node):
        if node != None:
            self._in_order_walk(node.leftChild)
            print node.key
            self._in_order_walk(node.rightChild)


class TreeNode:
    def __init__(self, key, left=None, right=None, parent=None, height=0):
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.height = height
