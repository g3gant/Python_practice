class Solution():
    def readSpiral(arr):
        lp,rp = 0,len(arr[0])
        tp,bp = 0,len(arr)
        res = []
        while lp<rp and tp<bp:
            
            #top horizontal pass
            for i in range(lp,rp):
                res.append(arr[tp][i])
            tp+=1

            #right col pass
            for i in range(tp,bp-1):
                res.append(arr[i][rp-1])
            rp-=1

            #bottom pass
            for i in range(rp,lp-1,-1):
                res.append(arr[bp-1][i])
            bp-=1
            
            #left column pass
            for i in range (bp-1,tp-1,-1):
                res.append(arr[i][lp])
            lp+=1
        
        return res


test_arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

#print (test_arr[0][0])
print (Solution.readSpiral(test_arr))
#print(test_arr[0][0])
#print(test_arr[0][1])
