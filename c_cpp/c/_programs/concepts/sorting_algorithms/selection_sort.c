#include <stdio.h>

int main(){

	int temp = 0;

	// Get int array from user
	printf("Enter 5 elements: \n");
	int arr[5];
	for(int i = 0; i<5; i++){
		scanf("%d", &arr[i]);
	}

	// Calculate size of entered array
	int arr_len = sizeof(arr) / sizeof(arr[0]);
	printf("\nSize of array is %d\n", arr_len);

	for(int i = 0 ; i<arr_len; i++){
		// each element compare
		for(int j = i+1; j<arr_len; j++){

			// swap if bigger
			if (arr[i] > arr[j]){
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}

	// Print array
	for (int i =0; i<arr_len; i++){
		printf("%d ", arr[i]);
	}
	printf("\n");
}
