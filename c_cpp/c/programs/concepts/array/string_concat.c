#include <stdio.h>

int main(){
	
	char name[] = "shubham";
	char sname[] = "mehetre";

	int len;
	int len2;

	// Length of name
	for (len = 0; name[len]; len++);
	// Length of sname
	for (len2 = 0; sname[len2]; len2++);

	// Concating
	for (int i =0; i<len; i++){
		name[len+i] = sname[i];
	}

	// Null terminating the full string
	name[len+len2] = '\0';

	// Printing the concated string
	for (int i =0; name[i]; i++){
		printf("%c", name[i]);
	}
	printf("\n");
}
