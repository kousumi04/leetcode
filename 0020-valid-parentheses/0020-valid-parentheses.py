class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close={")":"(", "}":"{", "]":"["}
        for char in s:
            # check if the char is present in the close dict
            if char in close:
                if stack and stack[-1]==close[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)    
        return True if not stack else False