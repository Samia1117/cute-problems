class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = sorted(list(s))
        t_list = sorted(list(t))
        
        return True if s_list == t_list else False
        
        
        
