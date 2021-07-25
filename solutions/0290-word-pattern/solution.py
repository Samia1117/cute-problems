class Solution:
    
    def wordPattern(self, pattern: str, s: str) -> bool:
        # pattern2 = "abba"
        # s2 = "dog cat cat fish"
        # pattern3 ="aaaa"
        # s3 = "dog cat cat dog"
        # pattern4 ="abba"
        # s4 = "dog dog dog dog"
        
        # print("first one")
        # print(self.wordPattern2(pattern2, s2))
        # print("second:")
        # print(self.wordPattern2(pattern3, s3))
        # print("third:")
        # print(self.wordPattern2(pattern4, s4))
        
        if len(pattern)!= len(s.split(" ")):
            return False
        
        letter_dict = dict()
        word_dict = dict()
        
        lidx = 0
        for letter in pattern:
            if letter not in letter_dict:
                letter_dict[letter] = []
            letter_dict[letter].append(lidx)
            lidx +=1
            
        widx = 0
        for word in s.split(" "):
            if word not in word_dict:
                word_dict[word] = []
            word_dict[word].append(widx)
            widx +=1
        
        #Lengths same, so assume first letter maps to first word and so on   
        # check the values associatd with parallel keys are same:
        
        wordlist=  list(word_dict.keys())  # letterlist[0] a 
        letterlist = list(letter_dict.keys()) # wordlist[0] dog 
        print(wordlist)
        print(letterlist)
        for i in range(len(wordlist)):
            if len( set(letter_dict[letterlist[i]]) - set(word_dict[wordlist[i]]) ) !=0 or len(set(word_dict[wordlist[i]]) - set(letter_dict[letterlist[i]]))!=0:
                return False
        
        return True
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
