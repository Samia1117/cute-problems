class Solution:

    digits_map = {
            '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], 
            '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']
    } 

    def combinations(self, remaining_digits):

        print("remaining digits = remaining digits")

        if not remaining_digits:
            return []

        if len(remaining_digits) == 1:
            return self.digits_map[remaining_digits]

        all_combs = []
        digit = remaining_digits[0]

        for letter in self.digits_map[digit]:
            remaining_combs = self.combinations(remaining_digits[1:])
            # print("remaining combs = ", remaining_combs)
            combs_with_curren_letter = [letter + x for x in remaining_combs]
            all_combs += combs_with_curren_letter
        
        return all_combs

        # print(f"Returning all_outputs_with_this_digits with digits={digits} is {all_outputs_with_this_digits}")
        return all_outputs_with_this_digits

    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        if len(digits) == 1:
            return self.digits_map[digits]

        all_combs = []
        digit = digits[0]

        for letter in self.digits_map[digit]:
            remaining_combs = self.letterCombinations(digits[1:])
            all_combs += [letter + x for x in remaining_combs]
        
        return all_combs
        
