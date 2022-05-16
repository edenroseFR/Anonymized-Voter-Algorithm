"""Accepts a voter's public key, and register it to the merkle_tree.

read about merkle_tree here: https://bit.ly/3szuTPO
watch about merkle_tree here: https://bit.ly/3Ng7vyK


"""


from typing import List
import hashlib

class Node:
    def __init__(self, left, right, value: str)-> None:
        self.left: Node = left
        self.right: Node = right
        self.value = value

    @staticmethod
    def hash(val: str)-> str:
        return hashlib.sha256(val.encode('utf-8')).hexdigest()

    @staticmethod
    def hashfunc(val: str, n=10)-> str:
        """Hash ::val ::n number of times"""
        
        for _ in range(n):
            val = Node.hash(val)

        return val
    
    
class MerkleTree:
    def __init__(self, values: List[str])-> None:
        self.__build_tree(values)

    def __build_tree(self, values: List[str])-> None:
        leaves: List[Node] = [Node(None, None, Node.hashfunc(e)) for e in values]
        if len(leaves) % 2 == 1:
            leaves.append(leaves[-1:][0]) # duplicate last elem if odd number of elements
        self.root: Node = self.__build_tree_rec(leaves)

    def __build_tree_rec(self, nodes: List[Node])-> Node:
        half: int = len(nodes) // 2

        if len(nodes) == 2:
            return Node(nodes[0], nodes[1], Node.hashfunc(nodes[0].value + nodes[1].value))

        left: Node = self.__build_tree_rec(nodes[:half])
        right: Node = self.__build_tree_rec(nodes[half:])
        value: str = Node.hashfunc(left.value + right.value)
        return Node(left, right, value)

    def print_tree(self)-> None:
        self.__print_tree_rec(self.root)

    def __print_tree_rec(self, node)-> None:
        if node != None:
            print(node.value)
            self.__print_tree_rec(node.left)
            self.__print_tree_rec(node.right)

    def get_root_hash(self)-> str:
        return self.root.value
    

def main()-> None:
    elems = ["Hello", "mister", "Merkle"]
    mtree = MerkleTree(elems)
    print(mtree.get_root_hash())


if __name__ == '__main__':
    main()
