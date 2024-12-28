#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int my_rand_func(int max){

	int random_number = (rand() % max) + 1;
	return random_number;
}
int main (){

	// adding seed value for randomness. 
	// PID is always randon hence choosing same for seed
	srand(getpid());

	// Getting max limit for random number
	int max;
	printf("Enter max limit: ");
	scanf("%d", &max);

	// Calling our random function
	int rand = my_rand_func(max);
	printf("\nRandom Number = %d\n", rand);

}
