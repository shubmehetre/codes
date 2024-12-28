#include <stdio.h>

int main(){
	printf("Enter number: ");
	int input;
	scanf("%d", &input);
	int store = input;

	for (int i=0; i<store; i++){

		for(int k = 0; k<i; k++)
			printf(" ");

		for (int j = input; j>0; j--){
			printf("* ");
		}
		
		input--;
		printf("\n");
	}


}
