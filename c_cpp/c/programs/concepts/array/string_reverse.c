#include <stdio.h>

int main (){

	char name[] = "shubham";
	// int name_len = sizeof(name) / sizeof(name[0]);
	int name_len=0;
	for (name_len=0; name[name_len];name_len++);
	printf("Length of name is %d\n", name_len);

	char new[name_len];

	// MAIN LOOP
	for (int i = 0 ; i<name_len; i++){
		// store in new
		new[i] = name[name_len - i - 1];
	}

	for(int i = 0; i<name_len; i++)
		printf("%c", new[i]);

	printf("\n");
}
