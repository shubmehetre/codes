#include <stdio.h>

int main(){
	printf("Enter number: ");
	int input;
	scanf("%d", &input);
	int store = input;

	for (int i = 0; i<input; i++){
		// print spaces
		// Eg. input=3, 
		// Spaces in 1st row = 3-1-0=2
		for (int j=input-1-i; j>0; j--)
			printf(" ");

		for (int k = 0; k<i+1; k++)
			printf("* ");

		printf("\n");
	}

}
