class TrieNode:
    def __init__(self):
        self.children={}
        self.val=0
class MapSum:

    def __init__(self):
        self.root=TrieNode()
        self.values={}
    def insert(self, key: str, val: int) -> None:
        old_val=self.values.get(key, 0)
        diff=val-old_val
        self.values[key]=val
        node=self.root
        for char in key:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
            node.val+=diff        

    def sum(self, prefix: str) -> int:
        node=self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node=node.children[char]
        return node.val        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)