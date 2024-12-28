#include<stdio.h>

int main(){

	int digit_store;
	int sum = 0;

	printf("Enter a number to reverse: ");
	scanf("%d", &digit_store);

	// 123
	// 321
	// 0 + 3 = 3
	// 30 + 2 = 32
	// 320 + 1 = 321

	while(digit_store > 0){
		sum = sum * 10 + digit_store%10;
		digit_store = digit_store / 10;
	}

	printf("Reverse order is %d\n", sum);
}
