# -*- coding: utf-8 -*-
# Given  an  arbitrary  ransom  note  string  and  another  string  containing  letters from  all  the  magazines, 
# write  a  function  that  will  return  true  if  the  ransom  note  can  be  constructed  from  the  magazines
#  otherwise,  it  will  return  false

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m = {}
        for c in magazine:
            m[c] = m.get(c, 0) + 1
        for c in ransomNote:
            if not m.get(c, 0):
                return False
            m[c] -= 1
        return True
        
