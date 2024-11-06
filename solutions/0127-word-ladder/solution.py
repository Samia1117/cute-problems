class Solution:

    def isEditDistance1(self, word1,  word2, distance):
        if distance > 1:
            return False
        elif distance == 1:
            if word1 == word2:
                return True
            return False
        else:    # distance = 0
            if not word1 or not word2:
                return False
            
            if word1 and word2 and word1[0] == word2[0]:
                return self.isEditDistance1(word1[1:],  word2[1:], distance)
            else:
                return self.isEditDistance1(word1[1:],  word2[1:], distance+1)
        return False

    def shortestPath(self, word, endword, wordList, visited, pathlength):
        # print("word, visited, pathlength = ", [word, visited, pathlength])

        if word == endword:
            return pathlength

        neighbors = [w for w in wordList if self.isEditDistance1(w, word, 0)]

        if not neighbors:
            return None    # no shortest path

        visited.add(word)
        shortest_path = 10000

        for neighbor in neighbors:
            if neighbor not in visited:
                path = self.shortestPath(neighbor, endword, wordlist, visited, pathlength+1)
                if path != None:
                    shortest_path = min(shortest_path, path)
        
        if shortest_path == 10000:
            shortest_path = None
        
        # print(f"Shortest path from word {word} to {endword} is {shortest_path}")
        return shortest_path

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # start at begin_word = current_word

        # look at all possible 'options' where option is a word that is both present in `wordList` and is 1 letter away from current_word

        # for each option, find the shortest ladder length to endWord 
            # question - should 
        # return min(option.shortestLadderLength for option in options)

        # Note that this can be modeled as 1) an undirected graph (can switch back and forth between two words as they are one character apart (e.g. hot -> hit, hit -> hot)) that can 2) have cycles (e.g. lot -> hot -> hit -> lit -> lot)

        q = deque()
        q.append((beginWord, 1))

        visited = {beginWord: False}

        shortestPath = None

        while q:
            word, level = q.popleft()
            if word == endWord:
                return level 
            neighbors = [w for  w in wordList if w not in visited and self.isEditDistance1(w, word, 0)]

            for neighbor in neighbors:
                if neighbor not in visited:
                    visited[neighbor] = True
                    q.append((neighbor, level + 1))

        return 0


