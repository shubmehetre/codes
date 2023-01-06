/*
Input:
N=5
S="RGRGR"

Output:
2
*/
#include <bits/stdc++.h>

using namespace std;

int main(){
  string x = "RRGGGRR";

  int r_count = 0, g_count = 0;

  for (int i = 0; i<x.size(); i++){
    if(x[i] == 'R'){
      r_count++;
    }
    else {
      g_count++;
    }
  }

  cout << min(r_count, g_count);

}
