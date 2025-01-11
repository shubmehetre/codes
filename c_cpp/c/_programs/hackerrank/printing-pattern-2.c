//https://www.hackerrank.com/challenges/printing-pattern-2/problem?isFullScreen=true

#include <stdio.h>

int main(){

	int n;
	scanf("%d", &n);

	int range = n*2-1;
	int start = 0;
	int end = range-1;
	int arr[range][range];

	while (n>0) {
	
		for (int i = start; i<=end; i++) {
			for (int j =start; j<=end; j++) {

				if(i==start || i==end || j==start || j==end){
					arr[i][j] = n;

				}
			
			}
		
		}

		++start;
		--end;
		--n;
	}
	// Print
	for (int i = 0; i<range; i++) {
		for (int j = 0; j<range; j++) {
			printf("%d ", arr[i][j]);
		}
			printf("\n");
	
	}


}
