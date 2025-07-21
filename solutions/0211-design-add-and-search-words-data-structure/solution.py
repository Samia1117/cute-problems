class WordDictionary:

    def __init__(self):
        self.trie = {}
        
    '''
    "act"
    trie = {}
    trie = {'a': {}, }
    trie = {'a': {'c'}, }
    trie = {'a': {'c': {'t':{}, 'e':{}, }, 'p': {}}, 'b': {..}}
    '''
    def addWord(self, word: str) -> None:
        # {a:{b:{o:{}, e:{}}}
        def rAddWord(word, trie):
            n = len(word)
            for i, w in enumerate(word):
                if w in trie:
                    trie = trie[w]
                else:
                    trie[w] = {}
                    trie = trie[w]
            # end of word, e.g. {'a': {'t': {'#':{}}, 's':{'k':{}, ..}, ..}}
            trie["#"] = {}

        rAddWord(word, self.trie)

    '''
    "act"
    "a.t"
        trie = {'a': {'c': {'t':{}, 'e':{}, }, 'p': {}}, 'b': {..}}
    '''
    def search(self, word: str) -> bool:
        def rsearch(word, trie, prin):
            for i, w in enumerate(word):
                if w in trie:
                    trie = trie[w]
                else:
                    if w == ".":
                    # print(f'word = {word}, word[i+1:] = {word[i+1:]}')
                        for elt in trie:
                            if rsearch(word[i+1:], trie[elt], True):
                                return True
                    return False
     
            return "#" in trie
        return rsearch(word, self.trie, False)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
