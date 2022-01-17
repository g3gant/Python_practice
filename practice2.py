# Found the most often character in the string
# Input is a string
# Output is max of character:count

class Solution():
    def getMaxChar(self, str):
        chrTable = self._getCharCountSimple(str)
        mostChar = max(chrTable,key=chrTable.get)
        #return mostChar + " : %s" % chrTable[mostChar]
        return (mostChar,chrTable[mostChar])

    def _getCharCount(self,str):
        charTable = {}
        count = 0
        for c in str:
            if charTable.get(c) != None:
                charTable[c] += 1
                
            else:
                count = 1
                charTable[c] = count
        return charTable


    def _getCharCountSimple(self,str):
        charTable = {}
        count = 0
        for c in str:
             charTable[c] = charTable[c]+1 if (charTable.get(c)) else 1
        return charTable

    def getCharTableRec(self,str,chrtbl):
        if len(str) == 0:
            return chrtbl
        c = str[0]
        chrtbl[c] = chrtbl[c]+1 if (chrtbl.get(c)) else 1
        return self.getCharTableRec(str[1:],chrtbl)



    def getCharTable(self,str):
        
        return sorted(self._getCharCountSimple(str).items(),key=lambda x:x[1],reverse=True)
    

sol = Solution()

#print(sol.getMaxChar("sdjhfovsahoenrfosivireoijoofpsdmhpitj[bhdfobsss"))
#print(sol.getCharTable("sdjhfovsahoenrfosivireoijoofpsdmhpitj[bhdfobsss"))
#key = {'a':1,'b':2}


print (sol.getCharTableRec("sdjhfovsahoenrfosivireoijoofpsdmhpitj[bhdfobsss",{}))
        