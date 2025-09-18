class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for w in word:
            if w not in trie:
                trie[w] = {}
            trie = trie[w]
        trie['#'] = {} # mark the end of the word 

    def search(self, word: str) -> bool:
        trie = self.trie
        for w in word:
            if w not in trie:
                return False
            trie = trie[w]
        if "#" in trie:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for w in prefix:
            if w not in trie:
                return False
            trie = trie[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
