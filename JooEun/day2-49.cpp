class Solution {
public:
    // sort all the given elements and, group them when they have the same sorted string pattern
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result; // 제출 vector
        
        // sort each string element to compare one another
        vector<string> sortedStr;
        for (string element: strs){
            string strCopy = element;
            sort(strCopy.begin(), strCopy.end()); // 정렬
            sortedStr.push_back(strCopy);
        }

        // brute force method => time limit 111/118 case passed
        // make string set that doesn't have duplication
        set<string> noDoubledStr;
        for(string ele : sortedStr){
            noDoubledStr.insert(ele);
        }

        // insert empty vector as many as the size of set that doesn't have duplication
        for(int i=0; i<noDoubledStr.size(); i++){
            vector<string> tmpArr;
            result.push_back(tmpArr);
        }
        
        for(int i=0; i<sortedStr.size(); i++){
            int j=0;
            set<string>::iterator iter;
            for(iter = noDoubledStr.begin(); iter != noDoubledStr.end(); iter++){
                if(sortedStr[i].compare(*iter)==0){
                    result[j].push_back(strs[i]);
                    break;
                }else{
                    j++;
                }
            }
        }

        
        return result;
    }
};
