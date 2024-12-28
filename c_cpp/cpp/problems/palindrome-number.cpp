// LINK: https://leetcode.com/problems/palindrome-number/

#include <bits/stdc++.h>
#include <stack>
#include <string.h>
#include <vector>
using namespace std;

class Solution {
public:
bool isPalindrome(int x) {

  int num = x;

  if (x < 0){
      return false;
  }

  else{
      double rev = 0;

      while(x!=0){
          rev = (rev * 10) + (x % 10);
          x = x / 10;
      }

      if (rev == num){
          return true;
      }
      else return false;
    }
  }
};
