#include<stdio.h>

int main (){

	int num;
	printf("Enter a number: ");
	scanf("%d", &num);

	// Logic: 9 % 2 == 0 (false, hence odd)
	
	// using if else
	if (num % 2 == 0){
		printf("\n%d is even", num);
	}else
		printf("\n%d is odd", num);

	printf("\nEnter a number again: ");
	scanf("%d", &num);

	// using ternary operators
	num % 2 == 0 ? printf("even\n") : printf("odd\n");

	return 0;
}
