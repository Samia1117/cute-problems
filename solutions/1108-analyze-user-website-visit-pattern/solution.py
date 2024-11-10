from itertools import combinations

class Solution:

    user_to_combs = {}

    def getAllSubstrings(self, user, length, substrings):
        if not substrings or len(subst):
            return []
        if len(substrings) == 3:
            # print(f"Returning substrings = {substrings} for user = {user}")
            self.user_to_combs.append(substrings)
        
        all_substrings1 = self.getAllSubstrings(user, length + 1, substrings[1:])   # use this word
        all_substrings2 = self.getAllSubstrings(user, length, substrings[1:])   # don't use this word
        
        return all_substrings1 + all_substrings2

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(website)
        if n <= 2:
            return []

        # iterate through the website, username, and timestamp lists if user not in dict, add user
        user_to_patterns = {}
        # 1. First gather all sequence of patterns per user

        processed_zipped_triplets = sorted(zip(username, website, timestamp), key = lambda x: x[2])
        # processed_zipped_triplets = sorted(processed_zipped_triplets1, key = lambda x: x[2])
        for user, ws, ts in processed_zipped_triplets:
            if user not in user_to_patterns:
                user_to_patterns[user] = []
            user_to_patterns[user].append(ws)

        counter = Counter()
        # 2. For each user's sequence, find a way to obtain 3-item ordered lists
        for k,v in user_to_patterns.items():
            combs = set(combinations(v, 3)) # print(f"user = {user}, combs = {combs}")
            counter.update(combs)
        
        print("Counter = ", list(counter))

        s = sorted(counter) 
        return max(sorted(counter), key=counter.get)
'''
        max_count, most_common_pattern = 0, None
        for pattern, cnt in counter.items():
            print("pattern, counter = ", [pattern, cnt])
            if cnt > max_count:
                max_count = cnt
                most_common_pattern = pattern
            
        return most_common_pattern

        # Try and exponential time algorithm, then optimize it 
'''
        
