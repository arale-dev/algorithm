class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        ans = ''
        if s[0] == '-':
            ans += '-'
            s = s[1:]
        ans += s[::-1]
        ans = int(ans)
        
        if (ans < -pow(2,31) or ans > (pow(2,31) - 1)):
            return 0
        return ans
        