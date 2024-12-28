#include <stdio.h>
#include <unistd.h>

int main (){

	// swap var without using temp
	int i, j;
	printf("Enter 2 nos: ");
	scanf("%d %d", &i, &j);

	printf("i = %d\nj = %d\n", i, j);
	printf("\nSwapped nos are: \n");

	i = i + j; // 10 + 5 = 15
	j = i - j; // j = 15 - 5 = 10
	i = i - j;


	printf("\ni = %d\nj = %d\n", i, j);
}
