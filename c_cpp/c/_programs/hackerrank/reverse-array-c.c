// https://www.hackerrank.com/challenges/reverse-array-c/problem?isFullScreen=true

#include <stdio.h>

int main(){
	int n;
	scanf("%d", &n);

	int arr[n];
	for (int i = 0; i<n; i++ ){
		scanf("%d", &arr[i]);
	}

	int rev[n];
	int temp = n;
	for (int i = 0; i<n; i++ ){
		rev[temp-1] = arr[i];
		temp--;
	}

	for (int i = 0; i<n; i++ ){
		printf("%d ", rev[i]);
	}
}
