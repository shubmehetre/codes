#include <stdio.h>

int factorial(int x){
	// fact = x * (x-1) * (x-2)...
	// fact = x * (x-1)!
	if (x==0)
		return 1;
	else{
		return (x * factorial(x-1));
	}
}

int main(){
	int x;
	printf("Enter a number: ");
	scanf("%d", &x);

	int answer = factorial(x);
	printf("Factorial of %d is %d\n", x,answer);
}
