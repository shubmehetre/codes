#include<stdio.h>

int main(){
	printf("Enter row size: ");
	int input;
	char magic = 'a';
	scanf("%d", &input);

	for (int i =0; i<input; i++){
		for (int j=0; j<=i; j++){

			printf("%c ", magic);

		}
		magic++;
		printf("\n");
	}
		printf("\n");
}

