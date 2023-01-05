// Author: Shubham A. Mehetre
#include <bits/stdc++.h>
using namespace std;

int main() {

  // arr [5] = {4,5,3,2,1}. Expected: {4,3,2,1}

  // vars req
  int size, num, temp;

  // get size of array
  cout << "Enter size of array req: ";
  cin >> size;

  // get the actual array of above size
  int arr[size];
  cout << "Enter array of size " << size << " : ";
  for (int i =0; i<size; i++){
    cin>> arr[i];
  }

  // get the number that is to be removed from the above array
  cout << "Enter number to be removed : ";
  cin >> num;

  // going through the array. taking the above element to the last
  for (int i = 0; i < size; i++) {

    // swap logic
    if (arr[i] == num) {
      temp = arr[i + 1];
      arr[i + 1] = num;
      arr[i] = temp;
    }
  }

  // Create new array 1 less size than above
  int arr2[size-1];

  // Put elements from arr to arr2. Last element will be skipped
  // as we allocated 1 less size to our new array
  for(int i = 0; i<size-1; i++){
    arr2[i] = arr[i];
  }

  // Print the final array. with the number to be removed, removed.
  for(int i = 0; i<size-1; i++){
    cout<<arr2[i]<< " ";
  }

}
