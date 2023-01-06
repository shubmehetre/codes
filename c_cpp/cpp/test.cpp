#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

int main() {

  // Strings test
  string x = "ASD";

  cout << *x.begin() << endl;
  cout << *(x.end()-1) << endl;

  reverse(x.begin(), x.end());
  reverse(x.begin(), x.end());


  cout << x[0] << endl;
  cout << x.at(0);


}
