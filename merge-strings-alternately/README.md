# Leetcode 1768. Merge Strings Alternately

**Problem link:** https://leetcode.com/problems/merge-strings-alternately/

## Description
Merge two strings by alternating letters from each, starting with the first string.  
If one string is longer, append the remaining letters to the end of the merged string.

## Solution idea
- Iterate through both strings simultaneously using an index.
- Append letters alternately from `word1` and `word2`.
- If one string ends before the other, append the remaining letters from the longer string.
- In Python, store characters in a list and finally join them with `"".join(list)`.

## Files
- `merge_alternately.py` — Python version, includes a local test with `if __name__ == "__main__":`

## Time and space complexity
- **Time complexity:** O(n + m), where n and m are the lengths of the two strings.
- **Space complexity:** O(n + m), as all characters are stored temporarily in a list/StringBuilder.