#include <stdio.h>

int main (){

	// Get int array from user
	printf("Enter 5 elements: \n");
	int arr[5];
	for(int i = 0; i<5; i++){
		scanf("%d", &arr[i]);
	}

	// Calculate size of entered array
	int arr_len = sizeof(arr) / sizeof(arr[0]);
	printf("\nSize of array is %d\n", arr_len);

	int temp = 0;
	// All cycles
	for(int j = 0; j<arr_len; j++){
		// Each cycle
		for (int i = 0; i<arr_len-1; i++){

			// Swap logic
			if(arr[i] > arr[i+1]){
				temp = arr[i];
				arr[i] = arr[i+1];
				arr[i+1] = temp;
			}
		}

	}

	// Print array
	for (int i =0; i<arr_len; i++){
		printf("%d ", arr[i]);
	}
	printf("\n");

}
