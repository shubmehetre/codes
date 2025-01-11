#include <stdio.h>

int main (){

	int arr[] = {1231,2245,345245,4123132,52342};
	int arr_len = sizeof(arr) / sizeof(arr[0]);

	int largest = arr[0];

	for (int i = 1 ; i< arr_len; i++){
		if (arr[i] > largest )
			largest = arr[i];
	}

	printf("\nLargest: %d\n", largest);
}
