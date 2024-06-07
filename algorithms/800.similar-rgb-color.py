class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def similar(s):
            ans = ''
            distance = None
            def convert(i):
                return '0123456789abcdef'[i]
            for i in range(16):
                
                temp = (s - (i*16 + i)) ** 2
                if distance == None or temp < distance:
                    distance = temp
                    ans = convert(i)*2
            return ans

        def to_number(s):
            return int(s, 16)
            
        ans = []
        for i in range(3):
            ans.append(similar(to_number(color[1+2*i:3+2*i])))
        return '#' + ''.join(ans)

color = '#09f166'
print(Solution().similarRGB(color))
