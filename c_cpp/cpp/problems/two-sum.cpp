// https://leetcode.com/problems/two-sum/

#include <bits/stdc++.h>
#include <stack>
#include <string.h>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<int> twoSum(vector<int>& nums, int target) {

      vector<int> answer;

      for (int i = 0 ; i<nums.size() ; i++){
        for (int j =i+1 ; j <nums.size() ; j++){
          if (nums[i] + nums[j] == target){
            answer.push_back(i);
            answer.push_back(j);
          }
        }
      }
        return answer;
    }
};
