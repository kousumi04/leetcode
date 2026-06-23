class Solution:
    def backspaceCompare(self, s, t):
        def process(string): 
            '''takes a string as input and 
            returns the final string after applying all backspaces.'''
            stack=[]  #empty list
            for ch in string: #for each ch in s or t
                if ch=="#":
                    if stack: # if found then pop
                        stack.pop()
                else:
                    stack.append(ch) #[bxj]
                    '''after '#' is found, the last element in the stack get appended'''
            return "".join(stack)
        '''takes all elements of a list of strings and 
        combines them into a single string with no space.'''
        #call function for both the strings
        return process(s)==process(t) 
                    
sol=Solution()
s="bxj##tw"
t="bxo#j##tw"
print(sol.backspaceCompare(s,t))

        