#include <stdio.h>

void double_for_logic(int, int);

int main(){
	printf("Enter number: ");
	int input;
	scanf("%d", &input);
	int store = input;

	double_for_logic(input, store);

}

void double_for_logic(int input, int store){

	for(int i = 0; i<input; i++){
		// Spaces for first pyramid
		for (int j = input-1-i; j>0; j--)
			printf(" ");

		for (int k = 0; k<i+1; k++)
			printf("* ");

		printf("\n");

	}

	for (int i = 0; i<=store; i++){
		// Spaces for second pyramid
		for (int j = 0; j<i+1; j++)
			printf(" ");

		for (int k = input-1-i; k>0; k--)
			printf("* ");

		store--;
		printf("\n");

	}

}
