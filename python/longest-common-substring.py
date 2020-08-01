# Longest Common Substring
# 中文English
# Given two strings, find the longest common substring.

# Return the length of it.

# Example
# Example 1:
# 	Input:  "ABCD" and "CBCE"
# 	Output:  2
	
# 	Explanation:
# 	Longest common substring is "BC"


# Example 2:
# 	Input: "ABCD" and "EACB"
# 	Output:  1
	
# 	Explanation: 
# 	Longest common substring is 'A' or 'C' or 'B'
# Challenge
# O(n x m) time and memory.

# Notice
# The characters in substring should occur continuously in original string. This is different with subsequence.

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        length = 0
        for i in range(len(A)):
            for j in range(i, len(A)):
                if A[i:j+1] in B and len(A[i:j+1]) >= length:
                    length = len(A[i:j+1])
        return length

#just using simple for loop to solve this. the substring need to be continuously characters, so we just use i to move one step each time, j loops from i to the end of the array to get all substring in A. Then each step we see whether that substring is in B and get the length. 
#Leetcode has a similar problem -- longest common sequence. but slightly different. --worth taking a look.
#the indices are 
