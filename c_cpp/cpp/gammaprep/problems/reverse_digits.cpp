#include <bits/stdc++.h>
using namespace std;

int main() {

  long long int x = 460100406171279; // revere: 1234

  string y = to_string(x);

  reverse(y.begin(), y.end());

  cout<< "reverse of 4321 is : " << (long long)stoi(y);

}
