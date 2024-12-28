#include <stdio.h>
#define F fflush(stdout)

int main (){
	int divisor_addition = 0;

	printf("Enter a number: "); F;
	int user_input;
	scanf("%d", &user_input);

	for (int i = 1; i<user_input; i++){

		if(user_input % i == 0){
			divisor_addition = divisor_addition + i;
		}
	}

	if (divisor_addition > user_input){
		printf("\nYes its Abundant\n");
	}else {
		printf("\nIts NOT Abundant\n");
	}
}
