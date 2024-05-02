class Trie:

    def __init__(self):
        # {'a':{ Trie({b: }), Trie({c:}),... }, 'b':{..}, .. }
        self.trie = {}
        

    def insert(self, word: str) -> None:
 
        if len(word) == 0:
            return

        current_trie = self.trie
        for ch in word:
            if ch not in current_trie:
                current_trie[ch] = {}
            current_trie = current_trie[ch]
        
        # reached end of word. Mark it so: "cat" -> "t":{"#":"#"}
        current_trie["#"] = "#"

    def search(self, word: str) -> bool:
        current_trie = self.trie

        n = len(word)
        if n == 0:
            return True

        for i in range(n):
            ch = word[i]
            if i == n-1 and ch in current_trie:
                children = current_trie[ch]
                if "#" in children:
                    # This is a word
                    return True
                else:
                    # This is not a word
                    return False
            else:
                if ch in current_trie:
                    current_trie = current_trie[ch]
                else:
                    return False
        # should never reach here
        return False
                

    def startsWith(self, prefix: str) -> bool:

        current_trie = self.trie
        if len(prefix) == 0:
            return True

        for ch in prefix:
            if ch in current_trie:
                current_trie = current_trie[ch]
            else:
                return False
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
