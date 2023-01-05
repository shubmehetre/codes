#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {

  // rewrite rotate array by n elements
  int size, rot;
  vector<int> v;
  vector<int> temp;

  cout << "\nEnter size of array: ";
  cin >> size;

  cout << "\nHow many times to rotate: ";
  cin >> rot;

  cout << "\nEnter the array: ";
  for (int i = 0 ; i<size; i++) {
    int data;
    cin>>data;
    v.push_back(data);
  }

  cout<< "\nYour array is : ";
  for (int i = 0 ; i<size; i++) {
    cout << v[i]<< " ";
  }


  // while (rot--) {
  //   v.push_back(*(v.begin()));
  // }


  for(int i = rot; i<size ; i++){
    temp.push_back(v[i]);
  }
  for(int i = 0; i<rot ; i++){
    temp.push_back(v[i]);
  }


  cout<< "\nRotated it " << rot << " times";
  for (int i = 0 ; i<size; i++) {
    cout<<" " <<temp[i];
  }


}
