# # first non-repeating element (hashmap)
# def firstUniqueElements(word):
#     unordered_map={}
#     for ch in word:
#         if ch in unordered_map:
#             unordered_map[ch]+=1
#         else:
#             unordered_map[ch]=1
#     for i in range(0, len(word)):
#         if unordered_map[word[i]]==1:
#             return word[i]        
#     return -1
# word=input("Enter a word: ")
# print(firstUniqueElements(word))


# finding frequency of elements
# def freqOfElements(word):
#     unordered_map={}
#     for ch in word:
#         if ch in unordered_map:
#             unordered_map[ch]+=1
#         else:
#             unordered_map[ch]=1
#     print(unordered_map.items())
#     return -1    
# word=input("Enter a word: ")
# freqOfElements(word)


# # finding occurrence of words
# def freqOfWords(sentence):
#     unordered_map={}
#     for word in sentence:
#         if word in unordered_map:
#             unordered_map[word]+=1
#         else:
#             unordered_map[word]=1    
#     print(unordered_map.items())
# sentence=input("Enter a word: ").split()
# freqOfWords(sentence)


# Find duplicate elements 
def findDuplicates(arr):
    unordered_map={}
    for ch in arr:
        if ch in unordered_map:
            unordered_map[ch]+=1
        else:
            unordered_map[ch]=1
    for i in range(0,len(arr)):
        if unordered_map[arr[i]]!=1:
            print(f"{arr} has duplicate elements.")
            break
        else:   
            print(f"{arr} doesn't contain any duplicate element.")
            break 
    return -1
arr=[1, 2, 3, 1, 2, 3]
findDuplicates(arr)