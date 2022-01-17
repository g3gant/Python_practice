def expandLeft(i,s):
    if (i-1>=0): return True
    else: return False

def expandRight(i,s):
    if (i+1<=len(s)-1): return True
    else: return False


def longestPalindrome(s):
    rl = rr = 0
    res = 0
    string = ""
    for i in range(len(s)):
        l=r=i
        
        pal = True
        while pal:
            
            if (s[l] != s[r]):
                pal = False
                continue
            
            if ((r-l+1)>res):
                res = max(res,r-l+1)
                rr = r
                rl = l
            if (expandLeft(l,s) or expandRight(r,s)):
                
                if (expandRight(r,s)):
                    if (s[r+1] == s[r]):
                        r+=1
                    else:
                        if (expandLeft(l,s)):
                            l-=1
                        r+=1
                else:
                   break 

            else:
                break
    
    for i in range(rl,rr+1):
        string+=s[i]           
    return string







s="aacabdkacaa"
print (longestPalindrome(s))

s= "babad"
print (longestPalindrome(s))

s="cbbd"
print (longestPalindrome(s))

s="222020221"
print (longestPalindrome(s))