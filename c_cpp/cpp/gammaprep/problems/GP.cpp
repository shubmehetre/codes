#include <bits/stdc++.h>

using namespace std;

int sum_of_gp(int n, int a, int d){

  int helper = a;
  int sum = 0;

  for (int i = 0; i< n ; i++){
    sum += helper;
    helper *= d;
  }


  return sum;

}

int main(){

  int n,a,d;
  cout << "Enter 3 nos as : number of terms, first term and common difference resp\n";

  cin>>n>>a>>d;

  int ans = sum_of_gp(n, a, d);

  cout << ans;

}
