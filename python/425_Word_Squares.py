import copy
class trieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        # use self.word to save the word ending at this node so that it's easy to retrieve
        self.word = None  
        
class trie:
    def __init__(self):
        self.root = trieNode()
        
    def insert(self, word):
        node = self.root
        for letter in word:
            child = trieNode()
            if letter not in node.children:
                node.children[letter] = child

            node = node.children[letter]
            
        node.isWord = True
        node.word = word
        
    def startWith(self, prefix):
        #coded this dfs to return all words that have the given prefix
        def search(node, res):
            if node.isWord == True:
                res.append(node.word)
                
            if not node.children:
                return
            
            for child in node.children:
                search(node.children[child], res)
            return 
        
        res = []
        node = self.root
        
        for p in prefix:
            if p not in node.children:
                return res
            node = node.children[p]
        
        search(node, res)

        return res    
            
            
class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        # write your code here
        if not words:
            return []
        tree = trie()
        for word in words:
            tree.insert(word)
        length = len(words[0])
        res = []
        
        # pick the first word
        for word in words:
            
            # index is for deciding the next word's prefix
            self.search_helper(1, tree, [word], res, length)
            
        return res
        
    def search_helper(self, index, tree, path, res, length):
        
        # if the length of path is already equal to length, then our job is done
        if len(path) == length:
            res.append(copy.copy(path))
            return 
        
        # update the prefix
        prefix = ''
        for p in path:
            prefix += p[index]
            
        # if there're no words having the given prefix, then we should go back and try other words
        if not tree.startWith(prefix):
            return 
        
        for w in tree.startWith(prefix):
            path.append(w)
            # everytime, index should increment by 1 to update the prefix
            self.search_helper(index + 1, tree, path, res, length)
            path.pop()
        return 
