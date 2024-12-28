#include <stdio.h>

int main(){
	// Get input from User
	int input;
	printf("Enter a number: ");
	scanf("%d", &input);
	int safe = input;
	
	int temp = 0;
	
	while(input > 0){
		temp = temp * 10 + input % 10;
		input /= 10;
	}

	if (temp == safe){
		printf("\nPALINDROME!!\n");
	}else
		printf("\nNOT!!\n");
}
