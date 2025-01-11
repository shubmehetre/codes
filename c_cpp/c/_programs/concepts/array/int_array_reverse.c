#include <stdio.h>

int main(){
	int arr[] = {1,2,3,4,5};
	int arr_len = sizeof(arr) / sizeof(arr[0]);
	printf("Array len is %d\n", arr_len);


	// Reverse 
	int temp = 0;
	int j = arr_len - 1;

	for (int i = 0; i<j; i++){
		temp = arr[i];

		arr[i] = arr[j];
		arr[j] = temp;

		j--;
	}


	printf("Reversed array = [ ");
	for(int i = 0; i<arr_len; i++){
		printf("%d ", arr[i]);
	}
	printf("]\n");
}
