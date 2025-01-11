// https://www.hackerrank.com/challenges/1d-arrays-in-c/problem?isFullScreen=true

#include <stdio.h>
#include <stdlib.h>

int main(){

	int n;
	int sum = 0;
	fflush(stdout);
	scanf("%d", &n);

	int *arr = malloc(n * sizeof(*arr));


	for (int i = 0; i<n; i++) {
		scanf("%d", &arr[i]);
	}

	
	for (int i =0; i<n; i++) {
		sum = sum + arr[i];
	}

	printf("%d", sum);
	free(arr);
}
