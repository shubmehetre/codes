#include<stdio.h>

int main(){

	int digit_store;
	int sum = 0;

	printf("Enter a number: ");
	scanf("%d", &digit_store);

	while(digit_store>0){
	sum = sum + digit_store%10;
	digit_store = digit_store/10;
	}

	printf("Sum of above digits = %d\n", sum);
}
