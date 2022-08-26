class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currentTrie = self.trie
        for i in range(len(word)):
            ch = word[i]
            if ch not in currentTrie:
                currentTrie[ch] = {}
            currentTrie = currentTrie[ch]
            
        currentTrie["."] = {}   # mark this as a word
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currentTrie = self.trie
        
        for i in range(len(word)):
            ch = word[i]
            if ch not in currentTrie:
                return False
            currentTrie = currentTrie[ch]
                
        return "." in currentTrie.keys()
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currentTrie = self.trie
                                  
        for i in range(len(prefix)):
            ch = prefix[i]
            if ch not in currentTrie:
                return False
            else:
                currentTrie = currentTrie[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
