// https://leetcode.com/problems/baseball-game/description/

class Solution
{
public:
  int calPoints(vector<string> &operations)
  {
    vector<int> numberArr; // record of calculations result/integer
    for (int i = 0; i < operations.size(); i++)
    {
      string tmp = operations[i];
      if (tmp.compare("C") == 0)
      {
        // invalidate the prev score
        if (numberArr.size() != 0)
        {
          numberArr.pop_back();
        }
        else
        {
          continue;
        }
      }
      else if (tmp.compare("D") == 0)
      {
        // double the prev score
        if (numberArr.size() != 0)
        {
          int tmpResult = numberArr.back() * 2;
          numberArr.push_back(tmpResult);
        }
        else
        {
          continue;
        }
      }
      else if (tmp.compare("+") == 0)
      {
        // sum of the prev two scores
        int tmpResult = 0;
        for (int k = numberArr.size() - 2; k < numberArr.size(); k++)
        {
          tmpResult += numberArr[k];
        }
        numberArr.push_back(tmpResult);
      }
      else
      {
        // only store integer
        int num = std::stoi(tmp);
        numberArr.push_back(num);
      }
    }

    // return the sum of all the scores on the record
    int tmpResult = 0;
    for (int k = 0; k < numberArr.size(); k++)
    {
      tmpResult += numberArr[k];
    }
    return tmpResult;
  }
};
