#include <bits/stdc++.h>

using namespace std;

int main (){
  string addr = "8.8.8.8"; // Expected: 8[.]8[.]8[.]8
  string answer = "";

  for (int i = 0 ; i<addr.size(); i++){

    if (addr[i] == '.') {
      answer += "[.]";

    }else {
      answer += addr[i];
    }

  }

  cout << "answer : " << answer;
}
