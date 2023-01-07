#include <bits/stdc++.h>
using namespace std;

int main() {

  string str = "4321";

  int len = str.size();
  int i;
  for (i = 0; i < len/2; i++)
  {
      char temp = str[i];
      str[i] = str[len-i-1];
      str[len-i-1] = temp;
  }

  cout << "reversed string : " << str;

}
