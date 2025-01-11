#include <stdio.h>

int main() {

	char arr[] = "Shubham";
	int len = sizeof(arr) / sizeof(arr[0]);


	for(int i = 0; i<len; i++){
		printf("%c ", arr[i]);
	}
	
	printf("\n");

}
