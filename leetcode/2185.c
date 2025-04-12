#include<stdio.h>

int main(){

	char *ptr;
	char names[100];

	for (int i = 0 ; i< 3; i++){
		fgets(names, 100, stdin);
	}
	for (int i = 0 ; i< 3; i++){
		fputs(names, stdin);
	}
}
