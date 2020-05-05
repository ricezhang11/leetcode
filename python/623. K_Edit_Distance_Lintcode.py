#### Lintcode VIP problem, don't have access. Run in local #####
#### Brute force: This problem is an extension of Lintcode 119. Edit Distance. 
#### We can compare every word in the string list with the target string and output every word that has an edit distance
#### smaller than k. However, the time complexity would be O(length(target) * length(word) * length(word list))

#### To avoid repeated efforts, we use trie to store common prefix together with 1d dp array (reduced dimentionality). 
#### Drawing a matrix using simple examples like "karma" to "mart" makes the solution much easier to understand. 

class trieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None

        
class trie:
    def __init__(self):
        self.root = trieNode()
        
# insert words into the trie
    def insert(self, word):
        node = self.root

        for w in word:
            if w not in node.children:
                child = trieNode()
                node.children[w] = child
            node = node.children[w]
            
# note whether a node is the end of a word and store the word
        node.isWord = True
        node.word = word


def k_edit_distance(words, target, k):
    tree = trie()
    
# insert all words into trie
    for word in words:
        tree.insert(word)
    node = tree.root
    length = len(target)
    dp = [0] * (length + 1)
    
# result list 
    res = []
    helper(node, target, dp, res, length, k)
    return res

# dp is the result of the last character of the tested word and the target word (last row in the matrix)
def helper(node, target, dp, res, length, k):
    if node.isWord == True and dp[length] <= k:
        res.append(node.word)

    if not node.children:
        return
    
    # this_dp: current row in the matrix. We will be populating the values of this row using the dp state function
    this_dp = [0] * (length + 1)
    # look at the children nodes one by one
    for child in node.children:
        # the first column of the matrix (always increment by 1)
        this_dp[0] = dp[0] + 1
        for i in range(1, length + 1):
            # if the characters are the same. Same dp state function as Edit Distance problem
            if child == target[i - 1]:
                this_dp[i] = min(this_dp[i - 1] + 1, dp[i] + 1, dp[i - 1])
            # if the characters are different. Same dp state function as Edit Distance problem
            else:
                this_dp[i] = min(this_dp[i - 1], dp[i], dp[i - 1]) + 1
        # keep iterating to the next character
        helper(node.children[child], target, this_dp, res, length, k)
    return
