// 2023.01.04 https://leetcode.com/problems/valid-sudoku
// brute force..

class Solution {
public:

    bool compare(char& a, char& b){
        return a < b;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        // row : n square
        for(int i=0; i<9; i++){
            int arr[9] = {1,1,1,1,1,1,1,1,1};
            for(int j=0; j<9; j++){
                int tmp = int(board[i][j]); // char to int : 1~9 숫자는 49~57
                // 숫자라면
                if(tmp >=49 && tmp <= 57){
                    tmp -= 48;
                    if(arr[tmp-1]!=-1){
                        arr[tmp-1] = -1;
                    }else{
                        return false;
                    }
                }
            }
        }

        // column : n square
        for(int i=0; i<9; i++){
            int arr[9] = {1,1,1,1,1,1,1,1,1};
            for(int j=0; j<9; j++){
                // 숫자라면
                int tmp = int(board[j][i]); // char to int : 1~9 숫자는 49~57
                if(tmp >=49 && tmp <= 57){
                    tmp -= 48;
                    if(arr[tmp-1]!=-1){
                        arr[tmp-1] = -1;
                    }else{
                        return false;
                    }
                }
            }
        }
        
        // box : n square / not 4 square lol
        for(int i=0; i<9; i+=3){
            for(int z=0; z<9; z+=3){
                int arr[9] = {1,1,1,1,1,1,1,1,1};
                for(int j=i; j<(i+3); j++){
                    for(int k=z;k<(z+3); k++){
                        // 숫자라면
                        int tmp = int(board[j][k]); // char to int : 1~9 숫자는 49~57
                        if(tmp >=49 && tmp <= 57){
                            tmp -= 48;
                            if(arr[tmp-1]!=-1){
                                arr[tmp-1] = -1;
                            }else{
                                return false;
                            }
                        }
                    }
                }
            }
        }

        return true;
    }
};
