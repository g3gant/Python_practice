def expandLeft(i,s):
    if (i-1>=0): return True
    else: return False

def expandRight(i,s):
    if (i+1<=len(s)-1): return True
    else: return False


def longestPalindrome(s):
    rl = rr = 0
    res = 0
    i = 0
    while ( i< len(s)):
        l=r=i
        
        pal = True

        while (expandRight(r,s) and s[r+1]==s[i]):
            r+=1
        skip = r-i

        while pal:
            
            if (s[l] != s[r]):
                pal = False
                continue
            
            if (res<r-l+1):
                rr=r
                rl=l
                res = max(res,r-l+1)

            if (expandRight(r,s) and expandLeft(l,s)):
                r+=1
                l-=1
            else:
                break
        i=i+1+skip        

    
        
    return s[rl:rr+1]







s="222020221"
print (longestPalindrome(s))

s="aacabdkacaa"
print (longestPalindrome(s))

s= "babad"
print (longestPalindrome(s))

s="cbbd"
print (longestPalindrome(s))