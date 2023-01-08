#include <bits/stdc++.h>
using namespace std;

int main() {

  long long arr[] = {1, 2, 3, 4, 5};
  int k = 3;
  int N = 5;

  for (int i = 0; i < N; i=i+k) {

    int start = i;
    int end = min(i + k - 1, N - 1);

    while (start <= end) {
      int temp = arr[start];
      arr[start] = arr[end];
      arr[end] = temp;

      start++;
      end--;
    }
  }

  for (int i = 0; i < N; i++) {
    cout << arr[i] << " ";
  }
}
