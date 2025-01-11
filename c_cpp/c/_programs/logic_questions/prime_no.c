// Prime no
#include <stdio.h>

int main(){

	// Get input
	printf("Enter a number: ");
	int num;
	scanf("%d", &num);
	int counter = 0;
	int i;

	for (i = 2; i<num; i++){
		if(num%i == 0)
			break;
	}

	printf("i is %d\n", i);

	if(num == i)
		printf("\nPrime\n");
	else
		printf("\nNot Prime\n");
	


}
