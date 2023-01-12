#include <bits/stdc++.h>

using namespace std;

int fact (int n){
  if (n ==1 || n ==0 ) return 1;

  return n*fact(n-1);

}

int main(){

  cout << "Enter a number: ";
  int n,r;
  cin>>n>>r;

  int ans = fact(n) / fact(n-r);

  cout << "Ans is : " << ans << endl;


}
