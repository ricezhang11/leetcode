class trieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None


class trie:
    def __init__(self):
        self.root = trieNode()

    def insert(self, word):
        node = self.root

        for w in word:
            if w not in node.children:
                child = trieNode()
                node.children[w] = child
            node = node.children[w]

        node.isWord = True
        node.word = word


def k_edit_distance(words, target, k):
    tree = trie()
    for word in words:
        tree.insert(word)
    node = tree.root
    length = len(target)
    dp = [0] * (length + 1)
    res = []
    helper(node, target, dp, res, length, k)
    return res


def helper(node, target, dp, res, length, k):
    if node.isWord == True and dp[length] <= k:
        res.append(node.word)

    if not node.children:
        return

    this_dp = [0] * (length + 1)
    for child in node.children:
        this_dp[0] = dp[0] + 1
        for i in range(1, length + 1):
            if child == target[i - 1]:
                this_dp[i] = min(this_dp[i - 1] + 1, dp[i] + 1, dp[i - 1])
            else:
                this_dp[i] = min(this_dp[i - 1], dp[i], dp[i - 1]) + 1
        helper(node.children[child], target, this_dp, res, length, k)
    return


def main():
    print(k_edit_distance(["abc", "abd", "abcd", "adc"], 'ac', 1))

main()
