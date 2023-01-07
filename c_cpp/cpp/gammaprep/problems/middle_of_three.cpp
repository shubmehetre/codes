#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main() {

  int a,b,c;

  cout << "Enter 3 nums : " ;
  cin >> a>>b>>c;


  if (a>b && b>c  ||  a<b && b<c) {
    cout << "Middle num : " << b;
  }
  else if (a>c && c>b  ||  a<c && c<b) {
    cout << "Middle num : " << c;
  }else{
    cout << "Middle num : " << a;
  }


}
