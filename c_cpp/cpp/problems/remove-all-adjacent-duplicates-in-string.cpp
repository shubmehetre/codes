// LINK: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

#include <bits/stdc++.h>
#include <stack>
#include <string.h>
using namespace std;

int main(){

  string s = "xyyxz";
  string answer= "";

  stack<char> ans;

  for (int i = 0; i<s.length(); i++){

    if ( (answer.size()) && (answer.back() == s[i]) ){
      answer.pop_back();
    }
    else{
        answer.push_back(s[i]);
      }
  }

  cout << answer;

}
