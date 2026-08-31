
class TrieNode:
    def __init__(self):
        self.children={}
        self.suggestions=[]
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root=TrieNode()
        for product in products:
            node=root
            for char in product:
                if char not in node.children:
                    node.children[char]=TrieNode()
                node=node.children[char]
                if len(node.suggestions)<3:
                    # add products
                    node.suggestions.append(product)
        result=[]
        node=root            
        for char in searchWord:
            if node is  None:
                result.append([])
            elif char not in node.children:
                node=None
                result.append([])
            else:
                node=node.children[char]
                result.append(node.suggestions) 
        return result           