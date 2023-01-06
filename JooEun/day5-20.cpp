// 2023.01.06 https://leetcode.com/problems/valid-parentheses

class Solution {
public:
    bool isValid(string s) {
        stack<char> bracket;
        for(char& c: s){
            if((c == '(') || (c == '[') || (c == '{')){
                bracket.push(c);
            }else{
                if(bracket.size() == 0) return false;
                char out = bracket.top();
                bracket.pop();
                if(((c == ')') && (out != '(')) 
                || ((c == '}') && (out != '{'))
                || ((c == ']') && (out != '[')) ){
                    return false;
                }
            }
        }
        if(bracket.size() != 0) return false;
        return true;
    }
};
