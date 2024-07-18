# 2023.01.11 https://leetcode.com/problems/longest-palindromic-substring/description/
# incomplete. not working in all cases

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        lst = []
        flag = 0
        if(len(s)==1):
            return s
        for i in range(len(s)):
            for j in range(len(s)-1,i, -1):
                if(s[i] == s[j]):
                    for k in range(i, (j-i)//2+1, 1):
                        if(s[k] != s[j +i - k]):
                            # print(s[k]+" "+s[j-k])
                            break
                        if(k ==(j//2) or k ==(j//2)-1):
                            # print(str(i)+" "+str(j))
                            flag = 1
                    if((j-i)==1 or (j-i)==0):
                        flag =1
                if(flag == 1):
                    for q in range(i, j+1):
                        result += s[q]
                    lst.append(result)
                    result =""
        
        if(len(lst)== 0):
            return s[0]
        else:
            lst.sort(key=lambda x:len(x))
            return lst[-1]
