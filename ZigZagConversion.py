class Solution:
    def convertByMod(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = ["" for _ in range(numRows)]
        for i,c in enumerate(s):
            mod = i % ((numRows-1)*2)
            mod = mod if mod < numRows else (numRows-1)*2-mod
            rows[mod] += c
        return ''.join(rows)

    def convertByDir(self, s: str, numRows: int) -> str:
        rows = ["" for _ in range(numRows)]
        l = len(s)
        step = 1
        cRow = 0
        for c in range(l):
            
            rows[cRow] += s[c]
            cRow+=step
            
            if cRow == numRows:
                cRow -= 2 
                step = -1
            
            if cRow == -1:
                cRow += 2
                step = 1
            
        return ''.join(rows)


s="PAYPALISHIRING"
#print(zigZag(s,3))
print(Solution().convertByDir(s,3))