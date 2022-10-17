#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
  int findDupli(vector<int> &nums){
    nums.push_back(1);
    nums.push_back(2);
    nums.push_back(3);

    cout << "in findDupli ";
    for (int i = 0; i < nums.size(); i++){
      cout << nums[i] << " " ;
    }
    cout<< endl;


    return 0;

  }
};

int main(){

  vector<int> arr ={1,3,4,2,2};

  vector<int>& nums = arr;

  Solution ob;
  ob.findDupli(nums);

  cout << "in MAIN ";
  for (int i = 0; i < nums.size(); i++){
    cout << nums[i] << " " ;
  }

}
