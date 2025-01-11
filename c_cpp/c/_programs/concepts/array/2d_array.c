// Test this with:
// https://pythontutor.com/render.html#mode=display

#include <stdio.h>

int main(){
	int arr[2][3] = {1,2,3,4,5,6};

	for (int i=0; i<2; i++) {
		for (int j =0; j<3; j++) {
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}

	printf("\n");

	int (*ptr_to_arr)[3] = arr;
	printf("arr is %p\n", arr);

	int *ptr_to_arr00 = &arr[0][0];
	printf("&arr[0] is %p\n", &arr[0][0]);

	int *ptr_to_star_arr = *arr;
	printf("*arr is %p\n", *arr);

	int *ptr_to_star_arr_plus_1 = *arr + 1;
	printf("*arr+1 is %p\n", *arr+1);

	int value_at_star_arr_stared = *(*arr);
	printf("*(*arr) is %d\n", *(*arr));

	int value_at_star_arr_plus_one_stared = *(*arr + 1);
	printf("*(*arr+1) is %d\n", *(*arr+1));

	int *ptr_to_arr_plus_1_stared = *(arr + 1);
	printf("*(arr+1) is %p\n", *(arr+1));

	int value_at_arr_plus_one_star_stared = **(arr+1);
	printf("**(arr+1) is %d\n", **(arr+1));

	int *ptr_to_arr_plus_one_stared_plus_2 = *(arr+1) +2;
	printf("*(arr+1)+2 is %p\n", *(arr+1)+2);

	int value_at_arr_plus_one_star_stared_plus2 = **(arr+1)+2;
	printf("**(arr+1)+2 is %d\n", **(arr+1)+2);
}
