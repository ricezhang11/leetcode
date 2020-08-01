# 71. Anagrams

# Given an array of strings, return all groups of strings that are anagrams.

# Example
# Example 1:

# Input:["lint", "intl", "inlt", "code"]
# Output:["lint", "inlt", "intl"]
# Example 2:

# Input:["ab", "ba", "cd", "dc", "e"]
# Output: ["ab", "ba", "cd", "dc"]
# Challenge
# What is Anagram?

# Two strings are anagram if they can be the same after change the order of characters.
# Notice
# All inputs will be in lower-case

class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        d = dict()
        if not strs:
            return strs
        for st in strs:
            res = ''.join(sorted(st))
            if res not in d.keys():
                d[res] = [st]
            else:
                d[res] = d[res] + [st]
        result = []
        for item in d.values():
            if len(item) >= 2:
                result = result + item
        
        return result

#sorted('abcd') will return a list of chars" ['a', 'b', 'c', 'd']
#therefore, we need to join the chars back together using ''.join()
#the solution is to sort each string and get the sorted string. Strings that are anagrams will have the same sorted string result. 
#use the sorted string as the key of the dictionary and values are lists of original strings. 
#to make the results a list of strings. Note that to use d[res] + [st] --- turn st into a list and then do list concatenation. 
 
