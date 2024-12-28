#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){

	printf("Enter T minus countdown number: \n");
	fflush(stdout);

	int num;
	scanf("%d", &num);

	while(num > 0){
		// printf("%d\n",num);
		num--;
		sleep(1);
		system("clear");
		printf("Enter T minus countdown number: \n");
		printf("%d\n",num);

	}

	printf("Time up!!!\n");

}

// 10

