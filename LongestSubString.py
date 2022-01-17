def Longest(s: str):
    l =0
    longest = 0
    seen= {}

    for r in range(len(s)):
        while  seen.get(s[r]):
            del seen[s[l]]
            l+=1
        seen[s[r]]=True
        longest = max(longest,r-l+1)
                
    return longest

s = 'aa123456bb'
print (Longest(s))