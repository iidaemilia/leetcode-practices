# Leetcode 1768. Merge Strings Alternately
#https://leetcode.com/problems/merge-strings-alternately/

def mergeAlternately(word1: str, word2: str)-> str:
    merged=[]
    i=0
    while i<len(word1) or i<len(word2):
        if i>=len(word1):
            merged.append(word2[i])
        elif i<len(word1) and i<len(word2):           
            merged.append(word1[i])
            merged.append(word2[i])
        elif i>=len(word2):
            merged.append(word1[i])
        i+=1          
    return "".join(merged)
if __name__=="__main__":
    print(mergeAlternately("koira","maukkakissa"))
