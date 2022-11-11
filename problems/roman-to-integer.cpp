// LINK: https://leetcode.com/problems/roman-to-integer/

#include <bits/stdc++.h>
#include <stack>
#include <string.h>
#include <unordered_map>
#include <vector>
using namespace std;


int main(){

  unordered_map<char, int> map{
    {'I', 1},
    {'V', 5},
    {'X', 10},
    {'L', 50},
    {'C', 100},
    {'D', 500},
    {'M', 1000},
  };


  string s = "XIV";
  int answer = 0;

  for(int i=0;i<s.size();i++){
    if(map[s[i]]<map[s[i+1]])
        answer-=map[s[i]];
    else
        answer+=map[s[i]];
  }
  cout << answer;
}
