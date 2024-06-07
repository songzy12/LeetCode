class Solution(object):
    def check(self, IP):
        if '.' in IP:
            return self.check4(IP)
        return self.check6(IP)
        
    def check4(self, IP):
        IP = IP.split('.')
        if not len(IP) == 4:
            return False
        def check(x):
            if not x.isdigit():
                return False
            if not 0 <= int(x) < 256:
                return False
            if len(str(int(x))) != len(x): # '01.01.01.01'
                return False
            return True                
        return all([check(x) for x in IP])
    
    def check6(self, IP):
        IP = IP.split(':')
        if not len(IP) == 8:
            return False
        def check(x):
            if len(x) > 4 or not len(x):
                return False            
            if not all([t in '0123456789abcdefABCDEF' for t in x]):
                return False
            return True
        return all([check(x) for x in IP])            
        
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        return "Neither" if not self.check(IP) else\
               "IPv4" if self.check4(IP) else\
               "IPv6"

IP = "abcd:0:0:0:0:0:0:0"
print Solution().validIPAddress(IP)
