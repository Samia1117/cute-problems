class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        trie_ptr = self.trie
        n = 0
        for char in word:
            if char not in trie_ptr:
                trie_ptr[char] = {}
            trie_ptr = trie_ptr[char]
        trie_ptr["word"] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        trie_ptr = self.trie
        for char in word:
            if char not in trie_ptr:
                return False
            trie_ptr = trie_ptr[char]
        if "word" in trie_ptr:
            return True
        return False
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        trie_ptr = self.trie
        for ch in prefix:
            if ch not in trie_ptr:
                return False
            trie_ptr = trie_ptr[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
