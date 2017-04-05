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

    def delete(self, z):
        if z.leftChild == None:
            self._transplant(z, z.rightChild)
        elif z.rightChild == None:
            self._transplant(z, z.leftChild)
        else:
            y = self.minimum(z.rightChild)

            if y.parent != z:
                self._transplant(y, y.rightChild)
                y.rightChild = z.rightChild
                y.rightChild.parent = y

            self._transplant(z, y)
            y.leftChild = z.leftChild
            y.leftChild.parent = y

    def _transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.leftChild:
            u.parent.leftChild = v
        else:
            u.parent.rightChild = v

        if v != None:
            v.parent = u.parent

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
        if root == None:
            x = self.root
        else:
            x = root

        while x.leftChild != None:
            x = x.leftChild

        return x

    def maximum(self, root=None):
        if root == None:
            x = self.root
        else:
            x = root

        while x.rightChild != None:
            x = x.rightChild

        return x

    def successor(self, node):
        if node.rightChild != None:
            return self.minimum(node.rightChild)

        y = node.parent

        while y != None and node == y.rightChild:
            x = y
            y = y.parent

        return y

    def predecessor(self, node):
        if node.rightChild != None:
            return self.minimum(node.leftChild)

        y = node.parent

        while y != None and node == y.leftChild:
            x = y
            y = y.parent

        return y

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
